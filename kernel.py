from datetime import datetime
import os
import shutil


class Kernel:

    def __init__(self):
        self.kernel_linux_folder = r"/usr/src/linux"
        self.kernel_linux_config_backup_folder = "kernel_config"
        self.date_time_stamp_string = None

    
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
            shutil.copyfile(r"/usr/src/linux/.config", destFileName)
            if os.path.isfile(destFileName):
                print("Everything worked as expected")
        except Exception as e:
            print(e)
    
    def create_working_env(self):
        desired_path = os.path.join(self.kernel_linux_folder, self.kernel_linux_config_backup_folder)
        if not os.path.isdir(desired_path):
            print("creating working dir")
            os.mkdir(desired_path)
        else:
            print("No need to create working directory because it already exists")
    
    def find_latest_backup_config(self):
        pass


kernelObj = Kernel()
kernelObj.backup_kernel_config()
