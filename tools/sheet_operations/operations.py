from typing import Optional
from server import mcp
from pygsheets import Worksheet
from constants.globals import Global
from constants.constants import Constants
from utils.utils import utility


@mcp.tool(name=Constants.LIST_SHEETS_NAME, description=Constants.LIST_SHEETS_DESC)
def list_sheets():
    """Returns a list of all worksheet names in the spreadsheet."""
    worksheets = Global.gc.worksheets()
    return [ws.title for ws in worksheets]


@mcp.tool(name=Constants.READ_SHEET_NAME, description=Constants.READ_SHEET_DESC)
def read_sheet(sheet_name: Optional[str] = None):
    """Returns the entire sheet"""
    sh:Worksheet= Global.gc.worksheet_by_title(sheet_name) or Global.gc.sheet1
    df = sh.get_as_df()
    res = df
    del df
    return res
    

@mcp.tool(name=Constants.CREATE_SHEET_NAME, description=Constants.CREATE_SHEET_DESC)
def create_sheet(sheet_name:str, row:Optional[int]=None, col:Optional[int]=None)->str:
    """Creates a new worksheet with optional row and column size."""
    if row and col: Global.gc.add_worksheet(title=sheet_name, rows=row, cols=col)
    else: Global.gc.add_worksheet(title=sheet_name)
    return f"Worksheet '{sheet_name}' added successfully."


@mcp.tool(name=Constants.DELETE_SHEET_NAME, description=Constants.DELETE_SHEET_DESC)
def delete_sheet(sheet_name:str)->str:
    """Deletes a worksheet by its name."""
    try:
        worksheet:Worksheet = Global.gc.worksheet_by_title(sheet_name)
        Global.gc.del_worksheet(worksheet)
        return f"Worksheet '{sheet_name}' deleted successfully."
    except Exception as e:
        return f"Error deleting sheet: {str(e)}"


@mcp.tool(name=Constants.RENAME_SHEET_NAME, description=Constants.RENAME_SHEET_DESC)
def rename_sheet(old_name:str, new_name:str)->str:
    """Renames an existing worksheet."""
    try:
        worksheet:Worksheet = Global.gc.worksheet_by_title(old_name)
        worksheet.title = new_name
        return f"Sheet '{old_name}' renamed to '{new_name}'"
    except Exception as e:
        return f"Error renaming sheet: {str(e)}"
