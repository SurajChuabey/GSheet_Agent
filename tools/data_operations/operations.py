from server import mcp
from constants.globals import Global
from pygsheets import Worksheet
from typing import Optional, Any,List

class DataOps:
    def __init__(self):
        pass

    @mcp.tool(name="read_range",description="Retrieves values from a specific rectangular range in the spreadsheet.")
    def read_range(start_cell: str, end_cell: str,sheet_name:Optional[str] = None):
        """
        Retrieves values from a specific rectangular range in the spreadsheet.
        
        :param start_cell: The top-left cell coordinate (e.g., "A1").
        :param end_cell: The bottom-right cell coordinate (e.g., "C10").
        :return: A list of lists representing the rows and columns within the range.
        """
        sh:Worksheet = Global.gc.worksheet_by_title(title=sheet_name) or Global.gc.sheet1 
        rtvl_data = sh.get_values(
            start=start_cell, 
            end=end_cell
        )
        return rtvl_data

    @mcp.tool(name="read_batch_ranges",description="Retrieves values from multiple non-contiguous ranges in a single request.")
    def read_batch_ranges(ranges: list[str],sheet_name:Optional[str] = None):
        """
        Retrieves values from multiple non-contiguous ranges in a single request.
        
        :param ranges: A list of A1 notation strings (e.g., ["A1:B2", "D5:E6", "Sheet2!A1"]).
        :return: A dictionary mapping each range to its 2D list of values.
        """
        try:
            sh:Worksheet = Global.gc.worksheet_by_title(title=sheet_name) or Global.gc.sheet1
            batch_data = sh.get_values_batch(ranges)
            result = {ranges[i]: batch_data[i] for i in range(len(ranges))}
            return result
        except Exception as e:
            return f"Error retrieving batch data: {str(e)}"
        
    @mcp.tool(name="update_row_by_index",description="Updates an entire row with new data based on the row number.")
    def update_row_by_index(row_index: int, values: list[Any],sheet_name:Optional[str] = None):
        """
        Updates an entire row with new data based on the row number.
        
        :param row_index: The 1-based index of the row to update (e.g., 1 for the first row).
        :param values: A list of values to insert into the row (e.g., ["val1", "val2", 300]).
        :return: Success message.
        """
        try:
            sh:Worksheet = Global.gc.worksheet_by_title(title=sheet_name) or Global.gc.sheet1
            start_cell = f"A{row_index}"
            sh.update_values(crange=start_cell, values=[values])
            return f"Row {row_index} updated successfully with {len(values)} columns."
        except Exception as e:
            return f"Error updating row {row_index}: {str(e)}"


    @mcp.tool(name="append_data_batch_in_rows",description="Appends multiple rows to a worksheet starting at the specified cell.If start value is not given then append in last")
    def append_data_batch_in_rows(start:str,values: list[list[Any]],sheet_name:Optional[str] = None):
        """
        Appends multiple rows to a worksheet starting at the specified cell.If start value is not given then append in last.

        Args:
            start (str): The starting cell (e.g., "A1") where the first row will be appended.
            values (list[list[Any]]): A list of rows, where each row is a list of cell values to append.

        Returns:
            str: A message indicating the number of rows successfully appended, or an error message if the operation fails.

        Raises:
            Exception: If appending the rows fails, an error message is returned.
        """
        try:
            sh:Worksheet = Global.gc.worksheet_by_title(title=sheet_name) or Global.gc.sheet1
            sh.append_table(values=values,start=start)
            return f"Successfully appended {len(values)} rows."
        except Exception as e:
            return f"Append failed: {str(e)}"


    @mcp.tool(name="read_sheet",description="Fetches every single populated row and column from the current worksheet.")
    def read_sheet(sheet_name:Optional[str] = None):
        """
        Fetches every single populated row and column from the current worksheet.
        
        :return: A complete 2D list of the entire sheet's data.
        """
        sh:Worksheet = Global.gc.worksheet_by_title(title=sheet_name) or Global.gc.sheet1
        all_records = sh.get_as_df()
        return all_records

    @mcp.tool(name="get_cell_value",description="Retrieves the value of a single specific cell.")
    def get_cell_value(cell_addr: str,sheet_name:Optional[str] = None):
        """
        Retrieves the value of a single specific cell.
        
        :param cell_addr: The A1 notation address of the cell (e.g., "B5").
        :return: The value contained in the cell.
        """
        sh:Worksheet = Global.gc.worksheet_by_title(title=sheet_name) or Global.gc.sheet1
        cell_val = sh.get_value(addr=cell_addr)
        return cell_val

    @mcp.tool(name="set_cell_value",description="Updates the value of a single specific cell.")
    def set_cell_value(cell_addr: str, value: Any,sheet_name:Optional[str] = None):
        """
        Updates the value of a single specific cell.
        
        :param cell_addr: The A1 notation address of the cell (e.g., "B5").
        :param value: The new value to place in the cell.
        :return: Confirmation message.
        """
        sh:Worksheet = Global.gc.worksheet_by_title(title=sheet_name) or Global.gc.sheet1
        sh.update_value(addr=cell_addr, val=value)
        return f"Value of Cell {cell_addr} updated successfully"

    @mcp.tool(name="clear_range",description="Deletes all content within a specified range of cells.")
    def clear_range(start_addr: str, end_addr: str,sheet_name:Optional[str] = None):
        """
        Deletes all content within a specified range of cells.
        
        :param start_addr: The top-left cell of the range to clear (e.g., "A1").
        :param end_addr: The bottom-right cell of the range to clear (e.g., "C10").
        :return: Confirmation message.
        """
        sh:Worksheet = Global.gc.worksheet_by_title(title=sheet_name) or Global.gc.sheet1
        sh.clear(start=start_addr, end=end_addr)
        return f"Values cleared from {start_addr}:{end_addr}"
    
    @mcp.tool(name="Update_or_Insert_Coloumn",description="Update or insert value in Column in one go")
    def update_coloumn(col_index:int,col_data:List[Any],sheet_name:Optional[str]):
        """
        This function selects a worksheet by its title if provided; otherwise,
        it defaults to the first worksheet in the spreadsheet. It then updates
        the specified column with the given list of values.

        Args:
            col_index (int): The column index to update.
            col_data (List[Any]): A list of values to write into the column.
            sheet_name (Optional[str]): The title of the worksheet to update.
                If None or not found, the first worksheet is used.

        Returns:
            str: A confirmation message indicating the column was updated successfully.
        """
        sh:Worksheet = Global.gc.worksheet_by_title(title=sheet_name) or Global.gc.sheet1
        sh.update_col(index=col_index,values=col_data)
        return f"Coloumn of index:{col_index} Updated successfully"