from datetime import datetime
import os
import shutil


class Kernel:

    def __init__(self):
        self.kernel_linux_folder = r"/usr/src/linux"
        self.kernel_linux_config_backup_folder = "kernel_config"
        self.last_working_kernel_dir = "last_working_config"
        self.date_time_stamp_string = None
        self.log_file_location = None

    
    def get_time_stamp(self):
        try:
            date_time_object = datetime.now()
            date_time_to_string = date_time_object.strftime("%d-%b-%Y_%H_%M_%S")
            self.date_time_stamp_string = date_time_to_string
            return self.date_time_stamp_string
        except Exception as e:
            print(e)

    def backup_kernel_config(self):
        try:
            self.get_time_stamp()
            fileName = ".config_" + self.date_time_stamp_string
            destFolderName = os.path.join(self.kernel_linux_folder, self.kernel_linux_config_backup_folder)
            destFileName = os.path.join(destFolderName, fileName)
            self.create_working_env()
            self.save_last_good_kernel_config()
            shutil.copyfile(r"/usr/src/linux/.config", destFileName)
            if os.path.isfile(destFileName):
                print("Everything worked as expected")
        except Exception as e:
            print(e)
    
    def create_working_env(self):
        desired_path = os.path.join(self.kernel_linux_folder, self.kernel_linux_config_backup_folder)
        working_path = os.path.join(self.kernel_linux_folder, self.last_working_kernel_dir)
        if not os.path.isdir(desired_path):
            print("creating config dir")
            try:
                os.mkdir(desired_path)
            except Exception as e:
                print(e)
        if not os.path.isdir(working_path):
            print("creating working directory")
            try:
                os.mkdir(working_path)
            except Exception as e:
                print(e)
    
    def save_last_good_kernel_config(self):
        path = os.path.join(self.kernel_linux_folder, self.last_working_kernel_dir)
        print("Is the current config file a working kernel config? (y/n) ")
        user_response = input()
        lowered_user_response = user_response.lower()
        if lowered_user_response == "y":
            orginal_config_file = os.path.join(self.kernel_linux_folder, ".config")
            backup_config_file = os.path.join(path, ".config")
            # this should do some sort of check to verify it wrote correclty but I am not wanting to do this today
            try:
                shutil.copyfile(orginal_config_file, backup_config_file)
            except Exception as e:
                print(e)
        else:
            pass

    def find_latest_backup_config(self):
        folderPath = os.path.join(self.kernel_linux_folder, self.kernel_linux_config_backup_folder)
        all_files = os.listdir(folderPath)
        config_files = []
        for all_file in all_files:
            if all_file.startswith(".config"):
                config_files.append(all_file)
        pass



kernelObj = Kernel()
kernelObj.backup_kernel_config()
#kernelObj.find_latest_backup_config()
