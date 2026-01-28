from typing import Optional
from server import mcp
from pygsheets import Worksheet
from constants.globals import Global
from utils.utils import utility
from constants.constants import Constants


@mcp.tool(name=Constants.SET_FORMULA_NAME, description=Constants.SET_FORMULA_DESC)
def set_formula_in_cell(sheet_name:str, cell_addr:str, formula:str)->str:
    """Inserts a Google Sheets formula into a specific cell."""
    sh:Worksheet = utility._get_worksheet(sheet_name=sheet_name)
    if not formula.startswith("="): formula="="+formula
    sh.update_value(addr=cell_addr, val=formula)
    return f"Formula set in {cell_addr}"


@mcp.tool(name=Constants.GET_FORMULA_NAME, description=Constants.GET_FORMULA_DESC)
def get_formula_from_cell(sheet_name:str, cell_addr:str):
    """Retrieves the formula string currently stored in a specific cell."""
    sh:Worksheet = utility._get_worksheet(sheet_name=sheet_name)
    return sh.get_value(addr=cell_addr, value_render="FORMULA")


@mcp.tool(name=Constants.EVALUATE_FORMULA_NAME, description=Constants.EVALUATE_FORMULA_DESC)
def evaluate_formula(sheet_name:str, cell_addr:str):
    """Retrieves the calculated result of a formula from a specific cell."""
    sh:Worksheet = utility._get_worksheet(sheet_name=sheet_name)
    return sh.get_value(addr=cell_addr, value_render="UNFORMATTED_VALUE")
