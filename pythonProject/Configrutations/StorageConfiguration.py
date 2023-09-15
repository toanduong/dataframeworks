import configparser
import os
from Configrutations.Configuration import IConfiguration
from Models.Configurations.StorageConfigModel import StorageConfigModel

class StorageConfiguration(IConfiguration):
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(os.path.join(os.path.dirname(__file__), "../config.ini"))

    def getConfig(self):
        data = self.config["StorageAccount"]
        return StorageConfigModel(**data)