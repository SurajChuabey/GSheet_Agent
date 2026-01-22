from pygsheets import Spreadsheet 
from pygsheets.client import Client
class Global:
    gc:Spreadsheet = None
    connection:Client = None