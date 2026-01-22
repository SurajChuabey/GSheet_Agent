import pygsheets,os
from constants.globals import Global
from constants.constants import Constants
from server import mcp

class Services:

    SERVICE_FILE_PATH = os.environ.get(Constants.SERVICE_FILE_PATH,default=Constants.DEFAULT_SERVICE_FILE_PATH)
        

    @staticmethod
    def connect():
        Global.connection = pygsheets.authorize(service_file=Services.SERVICE_FILE_PATH)   
        Global.gc = Global.connection.open(title="book")

@mcp.tool(name=Constants.SELECT_SHEET,description=Constants.SELECT_SHEET_DESC)
def select_sheet(sheet_name:str):
    """Open book with name which user specified"""
    Global.gc = Global.connection.open(title=sheet_name)