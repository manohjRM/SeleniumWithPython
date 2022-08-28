import configparser

config = configparser.RawConfigParser()
config.read("./config.ini")


class ReadConfig:
    @staticmethod
    def AppURL():
        url = config.get('common info', 'baseURL')
        return url
