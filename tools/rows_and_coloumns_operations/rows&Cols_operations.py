from typing import Optional
from server import mcp
from pygsheets import Worksheet
from constants.globals import Global
from constants.constants import Constants


@mcp.tool(name=Constants.INSERT_ROWS_NAME, description=Constants.INSERT_ROWS_DESC)
def insert_rows(sheet_name:str, row_index:int, count:int)->str:
    """Inserts `count` new rows starting at `row_index` (1-based)."""
    if sheet_name is None:sh = Global.gc.sheet1
    else:sh = Global.gc.worksheet_by_title(sheet_name)
    sh.insert_rows(row_index, number=count)
    return f"Inserted {count} rows starting at row {row_index}"


@mcp.tool(name=Constants.DELETE_ROWS_NAME, description=Constants.DELETE_ROWS_DESC)
def delete_rows(sheet_name:str, row_index:int, count:int)->str:
    """Deletes `count` rows starting at `row_index` (1-based)."""
    if sheet_name is None:sh = Global.gc.sheet1
    else:sh = Global.gc.worksheet_by_title(sheet_name)
    sh.delete_rows(row_index, number=count)
    return f"Deleted {count} rows starting at row {row_index}"


@mcp.tool(name=Constants.INSERT_COLUMNS_NAME, description=Constants.INSERT_COLUMNS_DESC)
def insert_columns(sheet_name:str, column_index:int, count:int)->str:
    """Inserts `count` new columns starting at `column_index` (1-based)."""
    if sheet_name is None:sh = Global.gc.sheet1
    else:sh = Global.gc.worksheet_by_title(sheet_name)
    sh.insert_cols(column_index, number=count)
    return f"Inserted {count} columns starting at column {column_index}"


@mcp.tool(name=Constants.DELETE_COLUMNS_NAME, description=Constants.DELETE_COLUMNS_DESC)
def delete_columns(sheet_name:str, column_index:int, count:int)->str:
    """Deletes `count` columns starting at `column_index` (1-based)."""
    if sheet_name is None:sh = Global.gc.sheet1
    else:sh = Global.gc.worksheet_by_title(sheet_name)
    sh.delete_cols(column_index, number=count)
    return f"Deleted {count} columns starting at column {column_index}"


@mcp.tool(name=Constants.HIDE_ROWS_NAME, description=Constants.HIDE_ROWS_DESC)
def hide_rows(sheet_name:str, row_indices:str)->str:
    """Hides rows using comma-separated indices (e.g. '2,5,7')."""
    if sheet_name is None:sh = Global.gc.sheet1
    else:sh = Global.gc.worksheet_by_title(sheet_name)
    rows=[int(r.strip()) for r in row_indices.split(",")]
    for r in rows: sh.hide_dimensions(r, r)
    return f"Hid rows: {rows}"


@mcp.tool(name=Constants.SHOW_ROWS_NAME, description=Constants.SHOW_ROWS_DESC)
def show_rows(sheet_name:str, row_indices:str)->str:
    """Unhides rows using comma-separated indices (e.g. '2,5,7')."""
    if sheet_name is None:sh = Global.gc.sheet1
    else:sh = Global.gc.worksheet_by_title(sheet_name)
    rows=[int(r.strip()) for r in row_indices.split(",")]
    for r in rows: sh.show_dimensions(r, r)
    return f"Unhid rows: {rows}"


@mcp.tool(name=Constants.HIDE_COLUMNS_NAME, description=Constants.HIDE_COLUMNS_DESC)
def hide_columns(sheet_name:str, column_indices:str)->str:
    """Hides columns using comma-separated indices (e.g. '1,3,5')."""
    if sheet_name is None:sh = Global.gc.sheet1
    else:sh = Global.gc.worksheet_by_title(sheet_name)
    cols=[int(c.strip()) for c in column_indices.split(",")]
    for c in cols: sh.hide_dimensions(c, c,dimension=Constants.COLUMNS)
    return f"Hid columns: {cols}"


@mcp.tool(name=Constants.SHOW_COLUMNS_NAME, description=Constants.SHOW_COLUMNS_DESC)
def show_columns(sheet_name:str, column_indices:str)->str:
    """Unhides columns using comma-separated indices (e.g. '1,3,5')."""
    if sheet_name is None:sh = Global.gc.sheet1
    else:sh = Global.gc.worksheet_by_title(sheet_name)
    cols=[int(c.strip()) for c in column_indices.split(",")]
    for c in cols: sh.show_dimensions(c, c,dimension=Constants.COLUMNS)
    return f"Unhid columns: {cols}"
