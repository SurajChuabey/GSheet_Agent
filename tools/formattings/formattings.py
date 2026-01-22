from typing import Optional
from constants.constants import Constants
from server import mcp
from utils.utils import utility


@mcp.tool(name=Constants.SET_TEXT_STYLE_NAME, description=Constants.SET_TEXT_STYLE_DESC)
def set_text_style(sheet_name:str, cell_range:str, bold:Optional[bool]=None, italic:Optional[bool]=None, font_size:Optional[int]=None)->str:
    """Sets bold, italic, and/or font size for the given cell range."""
    fmt={Constants.TEXT_FORMAT:{}}
    if bold is not None: fmt[Constants.TEXT_FORMAT][Constants.BOLD]=bold
    if italic is not None: fmt[Constants.TEXT_FORMAT][Constants.ITALIC]=italic
    if font_size is not None: fmt[Constants.TEXT_FORMAT][Constants.FONT_SIZE]=font_size
    utility._get_worksheet(sheet_name).apply_format(cell_range, fmt); return "Text style applied"


@mcp.tool(name=Constants.SET_TEXT_COLOR_NAME, description=Constants.SET_TEXT_COLOR_DESC)
def set_text_color(sheet_name:str, cell_range:str, r:int, g:int, b:int)->str:
    """Sets the text (font) color using RGB values (0-255)."""
    fmt={Constants.TEXT_FORMAT:{Constants.FOREGROUND_COLOR:utility.normalize_color((r,g,b))}}
    utility._get_worksheet(sheet_name).apply_format(cell_range, fmt); return "Text color applied"


@mcp.tool(name=Constants.SET_BACKGROUND_COLOR_NAME, description=Constants.SET_BACKGROUND_COLOR_DESC)
def set_background_color(sheet_name:str, cell_range:str, r:int, g:int, b:int)->str:
    """Sets the background (fill) color using RGB values (0-255)."""
    fmt={Constants.BACKGROUND_COLOR:utility.normalize_color((r,g,b))}
    utility._get_worksheet(sheet_name).apply_format(cell_range, fmt); return "Background color applied"


@mcp.tool(name=Constants.SET_ALIGNMENT_NAME, description=Constants.SET_ALIGNMENT_DESC)
def set_alignment(sheet_name:str, cell_range:str, h_align:Optional[str]=None, v_align:Optional[str]=None)->str:
    """Sets horizontal and/or vertical alignment of text inside cells."""
    fmt={}
    if h_align: fmt[Constants.H_ALIGN]=h_align.upper()
    if v_align: fmt[Constants.V_ALIGN]=v_align.upper()
    utility._get_worksheet(sheet_name).apply_format(cell_range, fmt); return "Alignment applied"


@mcp.tool(name=Constants.SET_WRAP_NAME, description=Constants.SET_WRAP_DESC)
def set_wrap(sheet_name:str, cell_range:str, wrap:str)->str:
    """Controls how text wraps inside cells (WRAP, CLIP, OVERFLOW)."""
    fmt={Constants.WRAP:wrap.upper()}
    utility._get_worksheet(sheet_name).apply_format(cell_range, fmt); return "Wrap applied"


@mcp.tool(name=Constants.SET_BORDERS_NAME, description=Constants.SET_BORDERS_DESC)
def set_borders(sheet_name:str, cell_range:str, style:str="SOLID")->str:
    """Applies borders around the given cell range using the specified style."""
    border={Constants.STYLE:style.upper()}
    fmt={Constants.BORDERS:{Constants.TOP:border,Constants.BOTTOM:border,Constants.LEFT:border,Constants.RIGHT:border}}
    utility._get_worksheet(sheet_name).apply_format(cell_range, fmt); return "Borders applied"


@mcp.tool(name=Constants.SET_ROTATION_NAME, description=Constants.SET_ROTATION_DESC)
def set_rotation(sheet_name:str, cell_range:str, angle:int)->str:
    """Rotates the text inside cells by the given angle in degrees."""
    fmt={Constants.TEXT_ROTATION:{Constants.ANGLE:angle}}
    utility._get_worksheet(sheet_name).apply_format(cell_range, fmt); return "Rotation applied"


@mcp.tool(name=Constants.SET_NUMBER_FORMAT_NAME, description=Constants.SET_NUMBER_FORMAT_DESC)
def set_number_format(sheet_name:str, cell_range:str, format_string:str)->str:
    """Sets number, date, currency, or percent format using a pattern string."""
    u=format_string.upper()
    t="DATE" if any(c in u for c in ["Y","M","D","H","S"]) else "PERCENT" if "%" in format_string else "CURRENCY" if "$" in format_string or "£" in format_string else "NUMBER"
    fmt={Constants.NUMBER_FORMAT:{Constants.TYPE:t,Constants.PATTERN:format_string}}
    utility._get_worksheet(sheet_name).apply_format(cell_range, fmt); return "Number format applied"


@mcp.tool(name=Constants.MERGE_CELLS_NAME, description=Constants.MERGE_CELLS_DESC)
def merge_cells(sheet_name:str, cell_range:str)->str:
    """Merges all cells in the given range into a single cell."""
    utility._get_worksheet(sheet_name).merge_cells(name=cell_range, merge_type="MERGE_ALL"); return f"Merged cells in {cell_range}"


@mcp.tool(name=Constants.SET_COLUMN_WIDTH_NAME, description=Constants.SET_COLUMN_WIDTH_DESC)
def set_column_width(sheet_name:str, column:int, width:Optional[int]=None)->str:
    """Sets the width of a column in pixels (or auto-fit if width is None)."""
    utility._get_worksheet(sheet_name).adjust_column_width(column, column, pixel_size=width); return "Column width updated"


@mcp.tool(name=Constants.SET_ROW_HEIGHT_NAME, description=Constants.SET_ROW_HEIGHT_DESC)
def set_row_height(sheet_name:str, row:int, height:Optional[int]=None)->str:
    """Sets the height of a row in pixels (or auto-fit if height is None)."""
    utility._get_worksheet(sheet_name).adjust_row_height(row, row, pixel_size=height); return "Row height updated"


@mcp.tool(name=Constants.AUTO_FIT_COLUMNS_NAME, description=Constants.AUTO_FIT_COLUMNS_DESC)
def auto_fit_columns(sheet_name:str, start_column:int, end_column:int)->str:
    """Automatically adjusts column widths based on cell content."""
    utility._get_worksheet(sheet_name).adjust_column_width(start_column, end_column); return "Columns auto-fitted"
