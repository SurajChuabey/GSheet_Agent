import pygsheets,os
from constants.globals import Global
from constants.constants import Constants

class Services:

    SERVICE_FILE_PATH = os.environ.get(Constants.SERVICE_FILE_PATH,default=Constants.DEFAULT_SERVICE_FILE_PATH)
        

    @staticmethod
    def connect():
        gc = pygsheets.authorize(service_file=Services.SERVICE_FILE_PATH)   
        Global.gc = gc.open(title="book")
