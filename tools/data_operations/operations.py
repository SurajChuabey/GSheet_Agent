from typing import Optional
from server import mcp
from constants.globals import Global
from constants.constants import Constants
from pygsheets import Worksheet
import csv
from utils.utils import utility
from io import StringIO


@mcp.tool(name=Constants.READ_RANGE_NAME, description=Constants.READ_RANGE_DESC)
def read_range(start_cell:str, end_cell:str, sheet_name:Optional[str]=None):
    """Retrieves values from a rectangular range like A1:C10."""
    sh:Worksheet = utility._get_worksheet(sheet_name=sheet_name)
    return sh.get_values(start=start_cell, end=end_cell)


@mcp.tool(name=Constants.READ_BATCH_RANGES_NAME, description=Constants.READ_BATCH_RANGES_DESC)
def read_batch_ranges(ranges:str, sheet_name:Optional[str]=None):
    """Retrieves values from multiple ranges (comma-separated, e.g. 'A1:B2,D5:E6')."""
    try:
        sh:Worksheet = utility._get_worksheet(sheet_name=sheet_name)
        range_list=[r.strip() for r in ranges.split(",")]
        batch_data=sh.get_values_batch(range_list)
        return {range_list[i]: batch_data[i] for i in range(len(range_list))}
    except Exception as e:
        return f"Error retrieving batch data: {str(e)}"


@mcp.tool(name=Constants.UPDATE_ROW_BY_INDEX_NAME, description=Constants.UPDATE_ROW_BY_INDEX_DESC)
def update_row_by_index(row_index: int, values: str, sheet_name: Optional[str] = None):
    """Updates a row using a CSV string. Handles quoted commas correctly."""
    try:
        sh: Worksheet = utility._get_worksheet(sheet_name=sheet_name)
        reader = csv.reader(StringIO(values))
        rows = [row for row in reader]
        
        if not rows:
            return "Error: No data provided."
        sh.update_values(crange=f"A{row_index}", values=[rows[0]])
        return f"Row {row_index} updated successfully."
    except Exception as e:
        return f"Error updating row {row_index}: {str(e)}"


@mcp.tool(name=Constants.APPEND_DATA_BATCH_IN_ROWS_NAME, description=Constants.APPEND_DATA_BATCH_IN_ROWS_DESC)
def append_data_batch_in_rows(values: str, start: Optional[str] = None, sheet_name: Optional[str] = None):
    """
    Appends multiple rows. 
    If 'start' is missing, it finds the first empty row automatically.
    """
    try:
        sh: Worksheet = utility._get_worksheet(sheet_name=sheet_name)
        
        reader = csv.reader(StringIO(values.strip()))
        rows = [row for row in reader]
        if not start:
            last_row = len(sh.get_all_values(include_tailing_empty_rows=False)) + 1
            start = f"A{last_row}"

        sh.update_values(start, rows)
        return f"Successfully appended {len(rows)} rows starting at {start}."
    except Exception as e:
        return f"Append failed: {str(e)}"

@mcp.tool(name=Constants.GET_CELL_VALUE_NAME, description=Constants.GET_CELL_VALUE_DESC)
def get_cell_value(cell_addr:str, sheet_name:Optional[str]=None):
    """Gets value of one cell like B5."""
    sh:Worksheet = utility._get_worksheet(sheet_name=sheet_name)
    return sh.get_value(addr=cell_addr)


@mcp.tool(name=Constants.SET_CELL_VALUE_NAME, description=Constants.SET_CELL_VALUE_DESC)
def set_cell_value(cell_addr:str, value:str, sheet_name:Optional[str]=None):
    """Sets value of one cell."""
    sh:Worksheet = utility._get_worksheet(sheet_name=sheet_name)
    sh.update_value(addr=cell_addr, val=value)
    return f"Value of cell {cell_addr} updated successfully"


@mcp.tool(name=Constants.CLEAR_RANGE_NAME, description=Constants.CLEAR_RANGE_DESC)
def clear_range(start_addr:str, end_addr:str, sheet_name:Optional[str]=None):
    """Clears all values in a range like A1:C10."""
    sh:Worksheet = utility._get_worksheet(sheet_name=sheet_name)

    sh.clear(start=start_addr, end=end_addr)
    return f"Values cleared from {start_addr}:{end_addr}"


@mcp.tool(name=Constants.UPDATE_COLUMN_NAME, description=Constants.UPDATE_COLUMN_DESC)
def update_column(col_index:int, values:str, sheet_name:Optional[str]=None):
    """Updates a column using comma-separated values."""
    sh:Worksheet = utility._get_worksheet(sheet_name=sheet_name)
    value_list=[v.strip() for v in values.split(",")]
    sh.update_col(index=col_index, values=value_list)
    return f"Column {col_index} updated successfully"
