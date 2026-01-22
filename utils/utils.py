from constants.globals import Global
from pygsheets import Worksheet
from typing import Tuple
class utility:

    @staticmethod
    def _get_worksheet(sheet_name: str) -> Worksheet:
        """Fetch worksheet by name. Defaults to sheet1 if empty or not found."""
        try:
            if not sheet_name:
                return Global.gc.sheet1
            return Global.gc.worksheet_by_title(sheet_name)
        except Exception:
            return Global.gc.sheet1

    
    @staticmethod
    def _list_to_a1(s_row: int, s_col: int, e_row: int, e_col: int) -> str:
        """
        Converts integer coordinates (1-based) into an A1 notation range string.
        """
        def col_to_letter(n):
            name = ""
            while n > 0:
                n, remainder = divmod(n - 1, 26)
                name = chr(65 + remainder) + name
            return name
        return f"{col_to_letter(s_col)}{s_row}:{col_to_letter(e_col)}{e_row}"
    
    @staticmethod
    def normalize_color(color_tuple:Tuple):
            if not color_tuple: return None
            return {
                'red': color_tuple[0] / 255.0 if color_tuple[0] > 1 else color_tuple[0],
                'green': color_tuple[1] / 255.0 if color_tuple[1] > 1 else color_tuple[1],
                'blue': color_tuple[2] / 255.0 if color_tuple[2] > 1 else color_tuple[2]
            }