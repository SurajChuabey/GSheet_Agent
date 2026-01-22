from typing import Optional
from server import mcp
from pygsheets import Worksheet
from constants.globals import Global
from constants.constants import Constants


@mcp.tool(name=Constants.SET_FORMULA_NAME, description=Constants.SET_FORMULA_DESC)
def set_formula_in_cell(sheet_name:str, cell_addr:str, formula:str)->str:
    """Sets a formula in a cell (e.g. '=SUM(A1:A10)')."""
    if sheet_name is None:sh = Global.gc.sheet1
    else:sh = Global.gc.worksheet_by_title(sheet_name)
    if not formula.startswith("="): formula="="+formula
    sh.update_value(addr=cell_addr, val=formula)
    return f"Formula set in {cell_addr}"


@mcp.tool(name=Constants.GET_FORMULA_NAME, description=Constants.GET_FORMULA_DESC)
def get_formula_from_cell(sheet_name:str, cell_addr:str):
    """Returns the formula string from a cell."""
    if sheet_name is None:sh = Global.gc.sheet1
    else:sh = Global.gc.worksheet_by_title(sheet_name)
    return sh.get_value(addr=cell_addr, value_render_option="FORMULA")


@mcp.tool(name=Constants.EVALUATE_FORMULA_NAME, description=Constants.EVALUATE_FORMULA_DESC)
def evaluate_formula(sheet_name:str, cell_addr:str):
    """Returns the evaluated result of a formula cell."""
    if sheet_name is None:sh = Global.gc.sheet1
    else:sh = Global.gc.worksheet_by_title(sheet_name)
    return sh.get_value(addr=cell_addr, value_render_option="UNFORMATTED_VALUE")
