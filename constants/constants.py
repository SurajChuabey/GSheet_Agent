class Constants:
    import os
    # env varibles
    SERVICE_FILE_PATH = 'SERVICE_FILE_PATH'



    # relative path 
    DEFAULT_SERVICE_FILE_PATH = os.environ.get("SERVICE_FILE_PATH",'./assets/pythonautomation-483215-d9363ca13b55.json')
    MCP_SERVER = "MCP SERVER"
    CONFIG_FILE_PATH = 'configurations/config.ini'

    # mcp configuration
    NAME = 'name'
    DESCRIPTION = 'description'
    INCLUDE_FASTMCP_META = 'include_fastmcp_meta'
    TRANSPORT = 'transport'
    MCP_HOST_DEFAULT = 'mcp_host'
    MCP_PORT_DEFAULT = 'mcp_port'
    VERSION = 'version'


    TEXT_FORMAT = "textFormat"
    FOREGROUND_COLOR = "foregroundColor"
    BACKGROUND_COLOR = "backgroundColor"

    BOLD = "bold"
    ITALIC = "italic"
    FONT_SIZE = "fontSize"

    H_ALIGN = "horizontalAlignment"
    V_ALIGN = "verticalAlignment"
    WRAP = "wrapStrategy"

    BORDERS = "borders"
    TOP = "top"
    BOTTOM = "bottom"
    LEFT = "left"
    RIGHT = "right"
    STYLE = "style"

    TEXT_ROTATION = "textRotation"
    ANGLE = "angle"

    NUMBER_FORMAT = "numberFormat"
    TYPE = "type"
    PATTERN = "pattern"

    COLUMNS = "COLUMNS"
    ROWS = "ROWS"


    READ_RANGE_NAME="read_range"; READ_RANGE_DESC="Retrieves values from a specific rectangular range in the spreadsheet."
    READ_BATCH_RANGES_NAME="read_batch_ranges"; READ_BATCH_RANGES_DESC="Retrieves values from multiple non-contiguous ranges in a single request."
    UPDATE_ROW_BY_INDEX_NAME="update_row_by_index"; UPDATE_ROW_BY_INDEX_DESC="Updates an entire row with new data based on the row number."
    APPEND_DATA_BATCH_IN_ROWS_NAME="append_data_batch_in_rows"; APPEND_DATA_BATCH_IN_ROWS_DESC="Appends multiple rows starting from a given cell."
    READ_SHEET_NAME="read_sheet"; READ_SHEET_DESC="Fetches every single populated row and column from the worksheet."
    GET_CELL_VALUE_NAME="get_cell_value"; GET_CELL_VALUE_DESC="Retrieves the value of a single specific cell."
    SET_CELL_VALUE_NAME="set_cell_value"; SET_CELL_VALUE_DESC="Updates the value of a single specific cell."
    CLEAR_RANGE_NAME="clear_range"; CLEAR_RANGE_DESC="Deletes all content within a specified range of cells."
    UPDATE_COLUMN_NAME="update_or_insert_column"; UPDATE_COLUMN_DESC="Updates or inserts values into a column."

    LIST_SHEETS_NAME="list_sheets"; LIST_SHEETS_DESC="Retrieves a list of all worksheet titles in the current spreadsheet."
    CREATE_SHEET_NAME="create_sheet"; CREATE_SHEET_DESC="Creates a new worksheet in the spreadsheet."
    DELETE_SHEET_NAME="delete_sheet"; DELETE_SHEET_DESC="Deletes an existing worksheet by its name."
    RENAME_SHEET_NAME="rename_sheet"; RENAME_SHEET_DESC="Renames an existing worksheet."

    INSERT_ROWS_NAME="insert_rows"; INSERT_ROWS_DESC="Inserts new rows starting from a given row index."
    DELETE_ROWS_NAME="delete_rows"; DELETE_ROWS_DESC="Deletes rows starting from a given row index."
    INSERT_COLUMNS_NAME="insert_columns"; INSERT_COLUMNS_DESC="Inserts new columns starting from a given column index."
    DELETE_COLUMNS_NAME="delete_columns"; DELETE_COLUMNS_DESC="Deletes columns starting from a given column index."
    HIDE_ROWS_NAME="hide_rows"; HIDE_ROWS_DESC="Hides specific rows."
    SHOW_ROWS_NAME="show_rows"; SHOW_ROWS_DESC="Unhides specific rows."
    HIDE_COLUMNS_NAME="hide_columns"; HIDE_COLUMNS_DESC="Hides specific columns."
    SHOW_COLUMNS_NAME="show_columns"; SHOW_COLUMNS_DESC="Unhides specific columns."

    
    SET_TEXT_STYLE_NAME = "set_text_style";SET_TEXT_STYLE_DESC = "Sets basic text styling such as bold, italic, and font size."
    SET_TEXT_COLOR_NAME = "set_text_color";SET_TEXT_COLOR_DESC = "Sets the text color of cells using RGB values (0-255)."
    SET_BACKGROUND_COLOR_NAME = "set_background_color";SET_BACKGROUND_COLOR_DESC = "Sets the background (fill) color of cells using RGB values (0-255)."
    SET_ALIGNMENT_NAME = "set_alignment";SET_ALIGNMENT_DESC = "Sets horizontal and/or vertical alignment of text."
    SET_WRAP_NAME = "set_wrap";SET_WRAP_DESC = "Controls how text wraps inside cells."
    SET_BORDERS_NAME = "set_borders";SET_BORDERS_DESC = "Applies borders around a range of cells."
    SET_ROTATION_NAME = "set_rotation";SET_ROTATION_DESC = "Rotates the text inside cells by a given angle."
    SET_NUMBER_FORMAT_NAME = "set_number_format";SET_NUMBER_FORMAT_DESC = "Sets the number/date/currency format for cells."
    MERGE_CELLS_NAME = "merge_cells";MERGE_CELLS_DESC = "Merges a range of cells into one."
    SET_COLUMN_WIDTH_NAME = "set_column_width";SET_COLUMN_WIDTH_DESC = "Sets the width of a column."
    SET_ROW_HEIGHT_NAME = "set_row_height";SET_ROW_HEIGHT_DESC = "Sets the height of a row."
    AUTO_FIT_COLUMNS_NAME = "auto_fit_columns";AUTO_FIT_COLUMNS_DESC = "Automatically fits column width to content."

    SET_FORMULA_NAME="set_formula_in_cell"; SET_FORMULA_DESC="Sets a formula in a specific cell."
    GET_FORMULA_NAME="get_formula_from_cell"; GET_FORMULA_DESC="Retrieves the formula from a specific cell."
    EVALUATE_FORMULA_NAME="evaluate_formula"; EVALUATE_FORMULA_DESC="Returns the evaluated (computed) value of a formula cell."
    
    CREATE_CHART_NAME="create_chart"; CREATE_CHART_DESC="Creates a chart (line, bar, pie, etc.) in a sheet."
    UPDATE_CHART_NAME="update_chart"; UPDATE_CHART_DESC="Updates an existing chart using its chart ID."
    DELETE_CHART_NAME="delete_chart"; DELETE_CHART_DESC="Deletes a chart using its chart ID."

    GET_SHEET_METADATA="get_sheet_metadata";GET_SHEET_METADATA_DESC="Give full info about sheet"

    SORT_RANGE_NAME="sort_range"; SORT_RANGE_DESC="Sorts data in a range by one or more columns."
    FILTER_DATA_NAME="filter_data"; FILTER_DATA_DESC="Applies filters to data in a range."
    REMOVE_DUPLICATES_NAME="remove_duplicates"; REMOVE_DUPLICATES_DESC="Removes duplicate rows from a range."
    FIND_VALUE_NAME="find_value"; FIND_VALUE_DESC="Searches for a specific value in a range."
    GET_UNIQUE_VALUES_NAME="get_unique_values"; GET_UNIQUE_VALUES_DESC="Returns unique values from a column."
    PIVOT_TABLE_CREATE_NAME="pivot_table_create"; PIVOT_TABLE_CREATE_DESC="Creates a pivot table from a source range."
    CREATE_PIVOT_NAME="create_gsheet_pivot"
    CREATE_PIVOT_DESC="Creates a pivot table in Google Sheets using Pandas-style logic."

    SELECT_SHEET="select_sheet";SELECT_SHEET_DESC="Helps user to change or select sheet by sheet name to perform operations"
    ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE = range(10)