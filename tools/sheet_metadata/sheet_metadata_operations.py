import json
from typing import Optional
from pygsheets.chart import Chart
from server import mcp
from pygsheets import Worksheet
from constants.globals import Global
from constants.constants import Constants

mcp.tool(name=Constants.GET_SHEET_METADATA,description=Constants.GET_SHEET_METADATA_DESC)
def get_sheet_metadata():
    """Returns metadata about sheets"""
    return  Global.gc.get_developer_metadata(search_sheets=True)