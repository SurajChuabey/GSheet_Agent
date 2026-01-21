from server import mcp
from typing import Optional, List
from pygsheets import Worksheet
from constants.globals import Global

class SheetOps:
    """
    A collection of tools for managing Google Sheets worksheets using pygsheets.
    """

    def __init__(self):
        pass

    
    @mcp.tool(name="list_sheets",description="Retrieves a list of all worksheet titles in the current spreadsheet.")
    def list_sheets() -> list[str]:
        """
        Retrieves a list of all worksheet titles in the current spreadsheet.
        
        Returns:
            list: A list of strings representing worksheet names.
        """
        worksheets:List[Worksheet] = Global.gc.worksheets()
        return [ws.title for ws in worksheets]
    
    
    @mcp.tool(name="create_sheet",description="Creates a new worksheet in the spreadsheet.")
    def create_sheet(sheet_name: str, row: Optional[int] = None, col: Optional[int] = None) -> str:
        """
        Creates a new worksheet in the spreadsheet.

        Args:
            sheet_name: The name of the new sheet.
            row: Optional number of rows (default is 1000).
            col: Optional number of columns (default is 26).
        """
        if row and col:
            Global.gc.add_worksheet(title=sheet_name, rows=row, cols=col)
        else:
            Global.gc.add_worksheet(title=sheet_name)
        return f"Worksheet '{sheet_name}' added successfully."
    
    @mcp.tool(name="delete_sheet",description="Deletes an existing worksheet by its name.")
    def delete_sheet(sheet_name: str) -> str:
        """
        Deletes an existing worksheet by its name.

        Args:
            sheet_name: The exact title of the worksheet to delete.
        """
        try:
            worksheet = Global.gc.worksheet_by_title(sheet_name)
            Global.gc.del_worksheet(worksheet)
            return f"Worksheet '{sheet_name}' deleted successfully."
        except Exception as e:
            return f"Error deleting sheet: {str(e)}"
    
    
    @mcp.tool(name="rename_sheet",description="Renames an existing worksheet.")
    def rename_sheet(old_name: str, new_name: str) -> str:
        """
        Renames an existing worksheet.

        Args:
            old_name: The current name of the worksheet.
            new_name: The new name to assign to the worksheet.
        """
        try:
            worksheet:Worksheet = Global.gc.worksheet_by_title(old_name)
            worksheet.title = new_name
            return f"Sheet '{old_name}' renamed to '{new_name}'"
        except Exception as e:
            return f"Error renaming sheet: {str(e)}"