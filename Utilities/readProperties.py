#this file used to read common data.
import configparser

#create object for configparser
config=configparser.RawConfigParser()

#Read the common values from config.ini file
config.read(".\\Configurations\config.ini")

class ReadConfig():

    @staticmethod
    def getApplicationURL():
        url=config.get('common info','baseURL')
        return url

    @staticmethod
    def getUserEmail():
        username = config.get('common info', 'useremail')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password