from typing import Optional
from server import mcp
from constants.globals import Global
from constants.constants import Constants
from pygsheets import Worksheet


@mcp.tool(name=Constants.READ_RANGE_NAME, description=Constants.READ_RANGE_DESC)
def read_range(start_cell:str, end_cell:str, sheet_name:Optional[str]=None):
    """Retrieves values from a rectangular range like A1:C10."""
    if sheet_name is None:sh = Global.gc.sheet1
    else:sh = Global.gc.worksheet_by_title(sheet_name)
    return sh.get_values(start=start_cell, end=end_cell)


@mcp.tool(name=Constants.READ_BATCH_RANGES_NAME, description=Constants.READ_BATCH_RANGES_DESC)
def read_batch_ranges(ranges:str, sheet_name:Optional[str]=None):
    """Retrieves values from multiple ranges (comma-separated, e.g. 'A1:B2,D5:E6')."""
    try:
        if sheet_name is None:sh = Global.gc.sheet1
        else:sh = Global.gc.worksheet_by_title(sheet_name)
        range_list=[r.strip() for r in ranges.split(",")]
        batch_data=sh.get_values_batch(range_list)
        return {range_list[i]: batch_data[i] for i in range(len(range_list))}
    except Exception as e:
        return f"Error retrieving batch data: {str(e)}"


@mcp.tool(name=Constants.UPDATE_ROW_BY_INDEX_NAME, description=Constants.UPDATE_ROW_BY_INDEX_DESC)
def update_row_by_index(row_index:int, values:str, sheet_name:Optional[str]=None):
    """Updates a row using comma-separated values (e.g. 'a,b,c,100')."""
    try:
        if sheet_name is None:sh = Global.gc.sheet1
        else:sh = Global.gc.worksheet_by_title(sheet_name)
        value_list=[v.strip() for v in values.split(",")]
        sh.update_values(crange=f"A{row_index}", values=[value_list])
        return f"Row {row_index} updated successfully."
    except Exception as e:
        return f"Error updating row {row_index}: {str(e)}"


@mcp.tool(name=Constants.APPEND_DATA_BATCH_IN_ROWS_NAME, description=Constants.APPEND_DATA_BATCH_IN_ROWS_DESC)
def append_data_batch_in_rows(start:str, values:str, sheet_name:Optional[str]=None):
    """Appends rows using 'a,b,c;1,2,3;4,5,6' format."""
    try:
        if sheet_name is None:sh = Global.gc.sheet1
        else:sh = Global.gc.worksheet_by_title(sheet_name)
        rows=[[v.strip() for v in row.split(",")] for row in values.split(";")]
        sh.update_values(start, rows)
        return f"Successfully appended {len(rows)} rows."
    except Exception as e:
        return f"Append failed: {str(e)}"

@mcp.tool(name=Constants.GET_CELL_VALUE_NAME, description=Constants.GET_CELL_VALUE_DESC)
def get_cell_value(cell_addr:str, sheet_name:Optional[str]=None):
    """Gets value of one cell like B5."""
    if sheet_name is None:sh = Global.gc.sheet1
    else:sh = Global.gc.worksheet_by_title(sheet_name)
    return sh.get_value(addr=cell_addr)


@mcp.tool(name=Constants.SET_CELL_VALUE_NAME, description=Constants.SET_CELL_VALUE_DESC)
def set_cell_value(cell_addr:str, value:str, sheet_name:Optional[str]=None):
    """Sets value of one cell."""
    if sheet_name is None:sh = Global.gc.sheet1
    else:sh = Global.gc.worksheet_by_title(sheet_name)
    sh.update_value(addr=cell_addr, val=value)
    return f"Value of cell {cell_addr} updated successfully"


@mcp.tool(name=Constants.CLEAR_RANGE_NAME, description=Constants.CLEAR_RANGE_DESC)
def clear_range(start_addr:str, end_addr:str, sheet_name:Optional[str]=None):
    """Clears all values in a range like A1:C10."""
    if sheet_name is None:sh = Global.gc.sheet1
    else:sh = Global.gc.worksheet_by_title(sheet_name)

    sh.clear(start=start_addr, end=end_addr)
    return f"Values cleared from {start_addr}:{end_addr}"


@mcp.tool(name=Constants.UPDATE_COLUMN_NAME, description=Constants.UPDATE_COLUMN_DESC)
def update_column(col_index:int, values:str, sheet_name:Optional[str]=None):
    """Updates a column using comma-separated values."""
    if sheet_name is None:sh = Global.gc.sheet1
    else:sh = Global.gc.worksheet_by_title(sheet_name)
    value_list=[v.strip() for v in values.split(",")]
    sh.update_col(index=col_index, values=value_list)
    return f"Column {col_index} updated successfully"
