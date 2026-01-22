import json
from typing import Optional
from server import mcp
from utils.utils import utility
from pygsheets import PyGsheetsException
from pygsheets import Worksheet
from constants.globals import Global
from constants.constants import Constants


@mcp.tool(name=Constants.SORT_RANGE_NAME, description=Constants.SORT_RANGE_DESC)
def sort_range(sheet_name:str, cell_range:str, sort_columns:str, ascending:Optional[bool]=True)->str:
    """Sorts a range by columns. sort_columns = '1,3' (1-based column indices)."""
    try:
        sh:Worksheet = utility._get_worksheet(sheet_name=sheet_name)
        cols=[int(c.strip()) for c in sort_columns.split(",")]
        sh.sort_range(cell_range, cols, ascending=ascending)
        return f"Sorted range {cell_range} by columns {cols}"
    except Exception as e:
        return f"Error sorting range: {str(e)}"


@mcp.tool(name=Constants.FILTER_DATA_NAME, description=Constants.FILTER_DATA_DESC)
def filter_data(sheet_name:str, cell_range:str, filter_criteria:str)->str:
    """Applies filters using JSON string. Example: {'column':1,'condition':'>','value':100}"""
    try:
        sh:Worksheet = utility._get_worksheet(sheet_name=sheet_name)
        criteria=json.loads(filter_criteria)
        sh.set_basic_filter(cell_range)
        return f"Filter applied on range {cell_range} (manual conditions via UI)."
    except Exception as e:
        return f"Error applying filter: {str(e)}"


@mcp.tool(name=Constants.REMOVE_DUPLICATES_NAME, description=Constants.REMOVE_DUPLICATES_DESC)
def remove_duplicates(sheet_name:str, cell_range:str, columns:str)->str:
    """Removes duplicates based on columns. columns='1,2' (1-based)."""
    try:
        sh:Worksheet = utility._get_worksheet(sheet_name=sheet_name)
        cols=[int(c.strip()) for c in columns.split(",")]
        sh.remove_duplicates(cell_range, cols)
        return f"Duplicates removed from {cell_range}"
    except Exception as e:
        return f"Error removing duplicates: {str(e)}"


@mcp.tool(name=Constants.FIND_VALUE_NAME, description=Constants.FIND_VALUE_DESC)
def find_value(sheet_name:str, search_value:str, cell_range:Optional[str]=None):
    """Finds all occurrences of a value in a range or entire sheet."""
    sh:Worksheet = utility._get_worksheet(sheet_name=sheet_name)
    return sh.find(search_value, matchEntireCell=False, searchByRegex=False, in_range=cell_range)


@mcp.tool(name=Constants.GET_UNIQUE_VALUES_NAME, description=Constants.GET_UNIQUE_VALUES_DESC)
def get_unique_values(sheet_name:str, column:int):
    """Returns unique values from a column (1-based)."""
    sh:Worksheet = utility._get_worksheet(sheet_name=sheet_name)
    values=sh.get_col(column)
    return list(set(values))


@mcp.tool(name=Constants.CREATE_PIVOT_NAME, description=Constants.CREATE_PIVOT_DESC)
def create_gsheet_pivot(spreadsheet_name:str, source_sheet_name:str, target_sheet_name:str, index_col:Optional[str]=None, columns_col:Optional[str]=None, agg_func:Optional[str]=None)->str:
    """Creates a pivot table in Google Sheets using Pandas pivot_table logic."""
    try:
        sh:Worksheet = Global.gc.worksheet_by_title(title=spreadsheet_name) or Global.gc.sheet1
        df = sh.get_as_df()

        if index_col is None or columns_col is None:
            return "Error: index_col and columns_col must be provided."

        ptable = df.pivot_table(index=index_col, columns=columns_col, aggfunc=agg_func)

        try:
            target_wks:Worksheet = Global.gc.add_worksheet(title=target_sheet_name)
        except Exception:
            target_wks = Global.gc.worksheet_by_title(target_sheet_name)
            target_wks.clear()

        target_wks.set_dataframe(ptable.reset_index(), start='A1')
        return f"Pivot table created successfully in '{target_sheet_name}'"

    except PyGsheetsException:
        return f"Error: Worksheet '{source_sheet_name}' not found."
    except Exception as e:
        return f"Error creating pivot table: {str(e)}"
