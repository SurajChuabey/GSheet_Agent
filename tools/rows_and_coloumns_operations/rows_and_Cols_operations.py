from server import mcp
from pygsheets import Worksheet
from constants.globals import Global
from utils.utils import utility
from constants.constants import Constants


@mcp.tool(name=Constants.INSERT_ROWS_NAME, description=Constants.INSERT_ROWS_DESC)
def insert_rows(sheet_name: str, row_index: int, count: int) -> str:
    """Inserts a specified number of empty rows at a given index."""
    sh: Worksheet = utility._get_worksheet(sheet_name=sheet_name)
    request = {
        Constants.INSERT_DIM: {
            Constants.RANGE: {
                Constants.PIVOT_SHEET_ID: sh.id,
                Constants.DIMENSION: Constants.ROWS,
                Constants.START_INDEX: row_index - 1,
                Constants.END_INDEX: (row_index - 1) + count
            },
            Constants.INHERIT_FROM_BEFORE: True
        }
    }
    Global.connection.sheet.batch_update(Global.gc.id,[request])
    return f"Inserted {count} rows starting at row {row_index}"

@mcp.tool(name=Constants.DELETE_ROWS_NAME, description=Constants.DELETE_ROWS_DESC)
def delete_rows(sheet_name: str, row_index: int, count: int) -> str:
    """Deletes a specified number of rows starting from a given index."""
    sh: Worksheet = utility._get_worksheet(sheet_name=sheet_name)
    request = {
        Constants.DELETE_DIM: {
            Constants.RANGE: {
                Constants.PIVOT_SHEET_ID: sh.id,
                Constants.DIMENSION: Constants.ROWS,
                Constants.START_INDEX: row_index - 1,
                Constants.END_INDEX: (row_index - 1) + count
            }
        }
    }
    Global.connection.sheet.batch_update(Global.gc.id,[request])
    return f"Deleted {count} rows starting at row {row_index}"

@mcp.tool(name=Constants.INSERT_COLUMNS_NAME, description=Constants.INSERT_COLUMNS_DESC)
def insert_columns(sheet_name: str, column_index: int, count: int) -> str:
    """Inserts a specified number of empty columns at a given index."""
    sh: Worksheet = utility._get_worksheet(sheet_name=sheet_name)
    request = {
        Constants.INSERT_DIM: {
            Constants.RANGE: {
                Constants.PIVOT_SHEET_ID: sh.id,
                Constants.DIMENSION: Constants.COLUMNS,
                Constants.START_INDEX: column_index - 1,
                Constants.END_INDEX: (column_index - 1) + count
            },
            Constants.INHERIT_FROM_BEFORE: True
        }
    }
    Global.connection.sheet.batch_update(Global.gc.id,[request])
    return f"Inserted {count} columns starting at column {column_index}"

@mcp.tool(name=Constants.DELETE_COLUMNS_NAME, description=Constants.DELETE_COLUMNS_DESC)
def delete_columns(sheet_name: str, column_index: int, count: int) -> str:
    """Deletes a specified number of columns starting from a given index."""
    sh: Worksheet = utility._get_worksheet(sheet_name=sheet_name)
    request = {
        Constants.DELETE_DIM: {
            Constants.RANGE: {
                Constants.PIVOT_SHEET_ID: sh.id,
                Constants.DIMENSION: Constants.COLUMNS,
                Constants.START_INDEX: column_index - 1,
                Constants.END_INDEX: (column_index - 1) + count
            }
        }
    }
    Global.connection.sheet.batch_update(Global.gc.id,[request])
    return f"Deleted {count} columns starting at column {column_index}"


@mcp.tool(name=Constants.HIDE_ROWS_NAME, description=Constants.HIDE_ROWS_DESC)
def hide_rows(sheet_name: str, row_indices: str) -> str:
    """Hides a list of specific rows in the worksheet."""
    sh: Worksheet = utility._get_worksheet(sheet_name=sheet_name)
    indices = [int(r.strip()) for r in row_indices.split(",")]
    
    requests = [{
        Constants.UPDATE_DIM_PROPS: {
            Constants.RANGE: {
                Constants.PIVOT_SHEET_ID: sh.id, 
                Constants.DIMENSION: Constants.ROWS, 
                Constants.START_INDEX: r - 1, 
                Constants.END_INDEX: r
            },
            Constants.PROPERTIES: {Constants.HIDDEN_BY_USER: True},
            Constants.FIELDS: Constants.HIDDEN_BY_USER
        }
    } for r in indices]
    
    Global.connection.sheet.batch_update(Global.gc.id, [requests])
    return f"Hid rows: {indices}"

@mcp.tool(name=Constants.SHOW_ROWS_NAME, description=Constants.SHOW_ROWS_DESC)
def show_rows(sheet_name: str, row_indices: str) -> str:
    """Unhides (shows) a list of specific rows in the worksheet."""
    sh: Worksheet = utility._get_worksheet(sheet_name=sheet_name)
    indices = [int(r.strip()) for r in row_indices.split(",")]
    
    requests = [{
        Constants.UPDATE_DIM_PROPS: {
            Constants.RANGE: {
                Constants.PIVOT_SHEET_ID: sh.id, 
                Constants.DIMENSION: Constants.ROWS, 
                Constants.START_INDEX: r - 1, 
                Constants.END_INDEX: r
            },
            Constants.PROPERTIES: {Constants.HIDDEN_BY_USER: False},
            Constants.FIELDS: Constants.HIDDEN_BY_USER
        }
    } for r in indices]
    
    Global.connection.sheet.batch_update(Global.gc.id, [requests])
    return f"Unhid rows: {indices}"

@mcp.tool(name=Constants.HIDE_COLUMNS_NAME, description=Constants.HIDE_COLUMNS_DESC)
def hide_columns(sheet_name: str, column_indices: str) -> str:
    """Hides a list of specific columns in the worksheet."""
    sh: Worksheet = utility._get_worksheet(sheet_name=sheet_name)
    indices = [int(c.strip()) for c in column_indices.split(",")]
    
    requests = [{
        Constants.UPDATE_DIM_PROPS: {
            Constants.RANGE: {
                Constants.PIVOT_SHEET_ID: sh.id, 
                Constants.DIMENSION: Constants.COLUMNS, 
                Constants.START_INDEX: c - 1, 
                Constants.END_INDEX: c
            },
            Constants.PROPERTIES: {Constants.HIDDEN_BY_USER: True},
            Constants.FIELDS: Constants.HIDDEN_BY_USER
        }
    } for c in indices]
    
    Global.connection.sheet.batch_update(Global.gc.id, [requests])
    return f"Hid columns: {indices}"

@mcp.tool(name=Constants.SHOW_COLUMNS_NAME, description=Constants.SHOW_COLUMNS_DESC)
def show_columns(sheet_name: str, column_indices: str) -> str:
    """Unhides (shows) a list of specific columns in the worksheet."""
    sh: Worksheet = utility._get_worksheet(sheet_name=sheet_name)
    indices = [int(c.strip()) for c in column_indices.split(",")]
    
    requests = [{
        Constants.UPDATE_DIM_PROPS: {
            Constants.RANGE: {
                Constants.PIVOT_SHEET_ID: sh.id, 
                Constants.DIMENSION: Constants.COLUMNS, 
                Constants.START_INDEX: c - 1, 
                Constants.END_INDEX: c
            },
            Constants.PROPERTIES: {Constants.HIDDEN_BY_USER: False},
            Constants.FIELDS: Constants.HIDDEN_BY_USER
        }
    } for c in indices]
    
    Global.connection.sheet.batch_update(Global.gc.id,[requests])
    return f"Unhid columns: {indices}"