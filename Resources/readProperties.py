import configparser

config = configparser.RawConfigParser()
config.read(".\\config.ini")


class ReadConfig:
    @staticmethod
    def app_url():
        url = config.get('common_info', 'baseURL')
        return url
