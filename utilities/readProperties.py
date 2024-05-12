import configparser
import os
import sys

os_name = sys.platform
file_path = ""
if os_name.startswith('darwin'):
    current_directory = os.getcwd()
    file_path = os.path.join(current_directory, "Configurations", "config.ini")
elif os_name.startswith('win'):
    file_path = ".\\Configurations\\config.ini"

config = configparser.RawConfigParser()
config.read(file_path)


class ReadConfig:
    @staticmethod
    def getCommonInfo(properties):
        return config.get('Common Info', properties)
