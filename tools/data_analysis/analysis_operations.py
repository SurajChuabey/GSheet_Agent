import json
import pandas as pd
from pandas import DataFrame
from typing import Optional,Union,List,Tuple
from server import mcp
from utils.utils import utility
from pygsheets import GridRange
from pygsheets import Worksheet
from constants.globals import Global
from constants.constants import Constants
from tools.sheet_operations.operations import read_sheet


@mcp.tool(name=Constants.SORT_RANGE_NAME, description=Constants.SORT_RANGE_DESC)
def sort_range(sheet_name: str,start:str,end:str,sort_columns:int,ascending:bool= True) -> str:
    """Sorts data in a specific range within a worksheet."""
    try:
        sh: Worksheet = utility._get_worksheet(sheet_name=sheet_name)
        sortorder = Constants.ACCENDING if ascending else Constants.DECCENDING
        sh.sort_range(start=start,end=end,basecolumnindex=sort_columns-1,sortorder=sortorder)
        return f"Sorted {start}:{end} by columns {sort_columns} (ascending={ascending})"
    except Exception as e:
        return f"Error sorting range: {e}"


@mcp.tool(name=Constants.FILTER_DATA_NAME, description=Constants.FILTER_DATA_DESC)
def filter_data(sheet_name: str, start: str, end: str, filter_criteria: str) -> str:
    """Applies complex filtering criteria to a range in a worksheet."""
    try:
        sh:Worksheet = utility._get_worksheet(sheet_name=sheet_name)
        criteria = json.loads(filter_criteria)
        
        # 1. Define the Range
        grid_range = GridRange.create(f"{start}:{end}", wks=sh).to_json()
        
        filter_specs = {}

        for col_index, config in criteria.items():
            idx = int(col_index) - Constants.ONE
            
            column_filter = {}
            
            # Value-based
            if Constants.HIDDEN_VALUE in config:
                column_filter[Constants.CONDITION] = {Constants.VALUES: [{Constants.USER_ENTERED_VALUE: v} for v in config[Constants.HIDDEN_VALUE]]}
            
            if Constants.TYPE in config:
                column_filter[Constants.CONDITION] = {
                    Constants.TYPE: config.get(Constants.TYPE),
                    Constants.VALUES: [{Constants.USER_ENTERED_VALUE: v} for v in config.get(Constants.VALUES, [])]
                }

            # Color filters
            if Constants.FILTER_FOREGROUND_COLOR in config:
                column_filter[Constants.FILTER_BACKGROUND_COLOR] = config[Constants.FILTER_FOREGROUND_COLOR]
            filter_specs[idx] = column_filter

        request = {
            Constants.SET_BASIC_FILTER: {
                Constants.FILTER: {
                    Constants.RANGE: grid_range,
                    Constants.CRITERIA: {str(k): v for k, v in filter_specs.items()}
                }
            }
        }
        Global.connection.sheet.batch_update(Global.gc.id, [request])

        return f"Applied multi-column filter to {start}:{end}."
        
    except Exception as e:
        return f"Error applying general filter: {str(e)}"


@mcp.tool(name=Constants.REMOVE_DUPLICATES_NAME, description=Constants.REMOVE_DUPLICATES_DESC)
def remove_duplicates(sheet_name: str,subset_columns: list[int] | None = None) -> str:
    """Removes duplicate rows from a worksheet based on specific columns."""
    try:
        sh = utility._get_worksheet(sheet_name=sheet_name)
        values = sh.get_all_values()

        header = values[Constants.ZERO]
        rows = values[Constants.ONE:]
        df = pd.DataFrame(rows, columns=header)

        # Remove duplicates
        cleaned_df = df.drop_duplicates(subset=[df.columns[i-Constants.ONE] for i in subset_columns]).copy()
        sh.clear()
        sh.set_dataframe(cleaned_df, start="A1", copy_head=True)
        return f"Removed duplicate rows from coloumns {[df.columns[i-Constants.ONE] for i in subset_columns]}'{sheet_name}'."
    except Exception as e:
        return f"Error removing duplicates: {str(e)}"


@mcp.tool(name=Constants.FIND_VALUE_NAME, description=Constants.FIND_VALUE_DESC)
def find_value(sheet_name:str, search_value:str, rows:Optional[Tuple] =None,cols:Optional[Tuple] = None):
    """Finds all occurrences of a value in a range or entire sheet.""" 
    sh:Worksheet = utility._get_worksheet(sheet_name=sheet_name)
    return sh.find(search_value, matchEntireCell=False, searchByRegex=False, rows=rows,cols=cols)


@mcp.tool(name=Constants.GET_UNIQUE_VALUES_NAME, description=Constants.GET_UNIQUE_VALUES_DESC)
def get_unique_values(sheet_name:str, column:int):
    """Returns unique values from a column (1-based)."""
    sh:Worksheet = utility._get_worksheet(sheet_name=sheet_name)
    values=sh.get_col(column)
    return list(set(values[1:]))


@mcp.tool(name=Constants.CREATE_PIVOT_NAME, description=Constants.CREATE_PIVOT_DESC)
def create_gsheet_pivot(source_sheet_name: str,target_sheet_name: str,index_col: str,value_col: str,agg_func: str = "AVERAGE",columns_col: Optional[str] = None) -> str:
    """Creates a pivot table in a target sheet based on source data."""
    try:
        source_wks:Worksheet = Global.gc.worksheet_by_title(source_sheet_name)
        values = source_wks.get_all_values()
        headers = values[Constants.ZERO]

        if index_col not in headers or value_col not in headers:
            return "Error: Invalid column names"

        index_idx = headers.index(index_col)
        value_idx = headers.index(value_col)
        columns_idx = headers.index(columns_col) if columns_col else None

        try:
            target_wks = Global.gc.add_worksheet(title=target_sheet_name)
        except Exception:
            target_wks = Global.gc.worksheet_by_title(target_sheet_name)
            target_wks.clear()

        pivot_table = {
            Constants.PIVOT_SOURCE: {
                Constants.PIVOT_SHEET_ID: source_wks.id,
                Constants.PIVOT_START_ROW_INDEX: 0,
                Constants.PIVOT_START_COLOUMN_INDEX: 0,
                Constants.PIVOT_END_ROW_INDEX: len(values),
                Constants.PIVOT_END_COLOUMN_INDEX: len(headers)
            },
            Constants.PIVOT_ROWS: [{
                Constants.PIVOT_SOURCE_COLOUMNOFF_SET: index_idx,
                Constants.PIVOT_SHOWTOTAL: True,
                Constants.PIVOT_SORT_ORDER: Constants.ACCENDING
            }],
            Constants.VALUES: [{
                Constants.PIVOT_SOURCE_COLOUMNOFF_SET: value_idx,
                Constants.PIVOT_SUMMARIZE_FUNCTION: agg_func.upper()
            }]
        }

        if columns_idx is not None:
            pivot_table[Constants.PIVOT_COLUMNS] = [{
                Constants.PIVOT_SOURCE_COLOUMNOFF_SET: columns_idx,
                Constants.PIVOT_SHOWTOTAL: True,
                Constants.PIVOT_SORT_ORDER: Constants.ACCENDING
            }]

        request = {
            Constants.PIVOT_UPDATE_CELLS: {
                Constants.START: {
                    Constants.PIVOT_SHEET_ID: target_wks.id,
                    Constants.PIVOT_ROW_INDEX: 0,
                    Constants.PIVOT_COLOUMN_INDEX: 0
                },
                Constants.PIVOT_ROWS: [{
                    Constants.VALUES: [{
                        Constants.PIVOT_TABLE: pivot_table
                    }]
                }],
                Constants.PIVOT_FIELD: Constants.PIVOT_TABLE
            }
        }

        Global.connection.sheet.batch_update(Global.gc.id,requests=[request])
        return f"Pivot table created successfully in '{target_sheet_name}'."
    except Exception as e:
        return f"Error creating pivot table: {str(e)}"
