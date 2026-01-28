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

    REQUESTS = "requests"
    FIELDS = "fields"
    PROPERTIES = "properties"

    CHART_TITLE = 'title'
    CHART_TYPE = 'chart_type'
    ANCHOR_CELL = 'anchor_cell'
    
    # --- Dimensions ---
    DIMENSION = "dimension"
    ROWS = "ROWS"
    COLUMNS = "COLUMNS"
    START_INDEX = "startIndex"
    END_INDEX = "endIndex"
    
    # --- Action Types ---
    UPDATE_DIM_PROPS = "updateDimensionProperties"
    INSERT_DIM = "insertDimension"
    DELETE_DIM = "deleteDimension"
    REPEAT_CELL = "repeatCell"
    SET_BASIC_FILTER = "setBasicFilter"
    
    # --- Formatting & Filtering Keys ---
    USER_ENTERED_FORMAT = "userEnteredFormat"
    USER_ENTERED_VALUE = "userEnteredValue"
    HIDDEN_BY_USER = "hiddenByUser"
    INHERIT_FROM_BEFORE = "inheritFromBefore"

    START = 'start'
    END = 'end'
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
    ACCENDING = 'ASCENDING'
    DECCENDING = "DESCENDING"

    TEXT_ROTATION = "textRotation"
    ANGLE = "angle"

    NUMBER_FORMAT = "numberFormat"
    TYPE = "type"
    PATTERN = "pattern"

    COLUMNS = "COLUMNS"
    ROWS = "ROWS"


    PIVOT_SOURCE = 'source'
    PIVOT_SHEET_ID = 'sheetId'
    PIVOT_START_ROW_INDEX = 'startRowIndex'
    PIVOT_START_COLOUMN_INDEX = 'startColumnIndex'
    PIVOT_END_ROW_INDEX = 'endRowIndex'
    PIVOT_END_COLOUMN_INDEX = 'endColumnIndex'
    PIVOT_ROWS = 'rows'
    PIVOT_SOURCE_COLOUMNOFF_SET = 'sourceColumnOffset'
    PIVOT_SHOWTOTAL = 'showTotals'
    PIVOT_SORT_ORDER = 'sortOrder'
    PIVOT_SUMMARIZE_FUNCTION = 'summarizeFunction'
    PIVOT_COLUMNS = 'columns'
    PIVOT_UPDATE_CELLS = 'updateCells'
    PIVOT_TABLE = 'pivotTable'
    PIVOT_FIELD = 'fields'
    PIVOT_ROW_INDEX = 'rowIndex'
    PIVOT_COLOUMN_INDEX = 'columnIndex'


    FILTER_BACKGROUND_COLOR = "filter_background_color"
    FILTER_FOREGROUND_COLOR = "filter_foreground_color"
    HIDDEN_VALUE = "hidden_values"
    SORT_ORDER = "sort_order"
    VALUES = 'values'
    SORT_COLOUMN_INDEX = 'sort_column_index'
    CRITERIA = 'criteria'
    CONDITION_TYPE = 'condition_type'
    CONDITION = 'condition'
    CONDITION_VALUES = 'condition_values'
    USER_ENTERED_VALUE ='userEnteredValue'
    SET_BASIC_FILTER ='setBasicFilter'
    FILTER = 'filter'
    RANGE = 'range'
    

    READ_RANGE_NAME="read_range"; READ_RANGE_DESC="Retrieves values from a specific rectangular range. Args: start_cell (e.g., 'A1'), end_cell (e.g., 'C10'), sheet_name (optional). Example: read_range('A1', 'B5')"
    READ_BATCH_RANGES_NAME="read_batch_ranges"; READ_BATCH_RANGES_DESC="Retrieves values from multiple non-contiguous ranges. Args: ranges (comma-separated, e.g., 'A1:B2,D5:E6'), sheet_name (optional). Example: read_batch_ranges('A1:A5,C1:C5')"
    UPDATE_ROW_BY_INDEX_NAME="update_row_by_index"; UPDATE_ROW_BY_INDEX_DESC="Updates an entire row with new data based on the row number. Args: row_index (1-based), values (CSV string), sheet_name (optional). Example: update_row_by_index(2, 'val1,val2,val3')"
    APPEND_DATA_BATCH_IN_ROWS_NAME="append_data_batch_in_rows"; APPEND_DATA_BATCH_IN_ROWS_DESC="Appends multiple rows starting from a given or automatic cell. Args: values (CSV string), start (optional, e.g., 'A1'), sheet_name (optional). Example: append_data_batch_in_rows('r1c1,r1c2\nr2c1,r2c2')"
    READ_SHEET_NAME="read_sheet"; READ_SHEET_DESC="Fetches every single populated row and column from the worksheet. Args: sheet_name (optional). Example: read_sheet('Sheet1')"
    GET_CELL_VALUE_NAME="get_cell_value"; GET_CELL_VALUE_DESC="Retrieves the value of a single specific cell. Args: cell_addr (e.g., 'A1'), sheet_name (optional). Example: get_cell_value('B2')"
    SET_CELL_VALUE_NAME="set_cell_value"; SET_CELL_VALUE_DESC="Updates the value of a single specific cell. Args: cell_addr (e.g., 'A1'), value (str), sheet_name (optional). Example: set_cell_value('C3', 'Hello')"
    CLEAR_RANGE_NAME="clear_range"; CLEAR_RANGE_DESC="Deletes all content within a specified range of cells. Args: start_addr (e.g., 'A1'), end_addr (e.g., 'C10'), sheet_name (optional). Example: clear_range('A1', 'B10')"
    UPDATE_COLUMN_NAME="update_or_insert_column"; UPDATE_COLUMN_DESC="Updates or inserts values into a column. Args: col_index (1-based), values (comma-separated str), sheet_name (optional). Example: update_column(1, 'v1,v2,v3')"

    LIST_SHEETS_NAME="list_sheets"; LIST_SHEETS_DESC="Retrieves a list of all worksheet titles in the current spreadsheet. No arguments required."
    CREATE_SHEET_NAME="create_sheet"; CREATE_SHEET_DESC="Creates a new worksheet. Args: sheet_name (str), row (optional int), col (optional int). Example: create_sheet('NewSheet', 100, 20)"
    DELETE_SHEET_NAME="delete_sheet"; DELETE_SHEET_DESC="Deletes an existing worksheet by its name. Args: sheet_name (str). Example: delete_sheet('OldSheet')"
    RENAME_SHEET_NAME="rename_sheet"; RENAME_SHEET_DESC="Renames an existing worksheet. Args: old_name (str), new_name (str). Example: rename_sheet('Sheet1', 'DataSheet')"

    INSERT_ROWS_NAME="insert_rows"; INSERT_ROWS_DESC="Inserts new empty rows. Args: sheet_name (str), row_index (1-based), count (int). Example: insert_rows('Sheet1', 5, 2)"
    DELETE_ROWS_NAME="delete_rows"; DELETE_ROWS_DESC="Deletes rows. Args: sheet_name (str), row_index (1-based), count (int). Example: delete_rows('Sheet1', 10, 5)"
    INSERT_COLUMNS_NAME="insert_columns"; INSERT_COLUMNS_DESC="Inserts new empty columns. Args: sheet_name (str), column_index (1-based), count (int). Example: insert_columns('Sheet1', 2, 3)"
    DELETE_COLUMNS_NAME="delete_columns"; DELETE_COLUMNS_DESC="Deletes columns. Args: sheet_name (str), column_index (1-based), count (int). Example: delete_columns('Sheet1', 1, 1)"
    HIDE_ROWS_NAME="hide_rows"; HIDE_ROWS_DESC="Hides specific rows. Args: sheet_name (str), row_indices (comma-separated, e.g., '1,2,5'). Example: hide_rows('Sheet1', '10,11,12')"
    SHOW_ROWS_NAME="show_rows"; SHOW_ROWS_DESC="Unhides specific rows. Args: sheet_name (str), row_indices (comma-separated, e.g., '1,2,5'). Example: show_rows('Sheet1', '10')"
    HIDE_COLUMNS_NAME="hide_columns"; HIDE_COLUMNS_DESC="Hides specific columns. Args: sheet_name (str), column_indices (comma-separated, e.g., '1,2'). Example: hide_columns('Sheet1', '1,2')"
    SHOW_COLUMNS_NAME="show_columns"; SHOW_COLUMNS_DESC="Unhides specific columns. Args: sheet_name (str), column_indices (comma-separated, e.g., '1,2'). Example: show_columns('Sheet1', '3')"

    
    SET_TEXT_STYLE_NAME = "set_text_style";SET_TEXT_STYLE_DESC = "Sets text styling. Args: sheet_name (str), cell_range (e.g., 'A1:C1'), bold (bool), italic (bool), font_size (int). Example: set_text_style('Sheet1', 'A1:B2', bold=True, font_size=12)"
    SET_TEXT_COLOR_NAME = "set_text_color";SET_TEXT_COLOR_DESC = "Sets text color using RGB. Args: sheet_name (str), cell_range (e.g., 'A1'), r (0-255), g (0-255), b (0-255). Example: set_text_color('Sheet1', 'A1', 255, 0, 0)"
    SET_BACKGROUND_COLOR_NAME = "set_background_color";SET_BACKGROUND_COLOR_DESC = "Sets background color using RGB. Args: sheet_name (str), cell_range (e.g., 'A1'), r (0-255), g (0-255), b (0-255). Example: set_background_color('Sheet1', 'A1:C10', 0, 255, 0)"
    SET_ALIGNMENT_NAME = "set_alignment";SET_ALIGNMENT_DESC = "Sets text alignment. Args: sheet_name (str), cell_range (e.g., 'A1'), h_align (LEFT/CENTER/RIGHT), v_align (TOP/MIDDLE/BOTTOM). Example: set_alignment('Sheet1', 'A1', h_align='CENTER')"
    SET_WRAP_NAME = "set_wrap";SET_WRAP_DESC = "Controls text wrapping. Args: sheet_name (str), cell_range (str), wrap (WRAP/CLIP/OVERFLOW). Example: set_wrap('Sheet1', 'A1:A5', 'WRAP')"
    SET_BORDERS_NAME = "set_borders";SET_BORDERS_DESC = "Applies borders. Args: sheet_name (str), cell_range (str), style (SOLID/DASHED/etc). Example: set_borders('Sheet1', 'B2:C3', 'SOLID')"
    SET_ROTATION_NAME = "set_rotation";SET_ROTATION_DESC = "Rotates text inside cells. Args: sheet_name (str), cell_range (str), angle (int, -90 to 90). Example: set_rotation('Sheet1', 'A1', 45)"
    SET_NUMBER_FORMAT_NAME = "set_number_format";SET_NUMBER_FORMAT_DESC = "Sets number/date format. Args: sheet_name (str), cell_range (str), format_string (pattern, e.g., '0.00', 'dd/mm/yyyy'). Example: set_number_format('Sheet1', 'A1', '0.00%')"
    MERGE_CELLS_NAME = "merge_cells";MERGE_CELLS_DESC = "Merges a range of cells. Args: sheet_name (str), start_range (e.g., 'A1'), end_range (e.g., 'C1'). Example: merge_cells('Sheet1', 'A1', 'C1')"
    SET_COLUMN_WIDTH_NAME = "set_column_width";SET_COLUMN_WIDTH_DESC = "Sets column width. Args: sheet_name (str), column (1-based int), width (pixels). Example: set_column_width('Sheet1', 1, 200)"
    SET_ROW_HEIGHT_NAME = "set_row_height";SET_ROW_HEIGHT_DESC = "Sets row height. Args: sheet_name (str), row (1-based int), height (pixels). Example: set_row_height('Sheet1', 2, 50)"
    AUTO_FIT_COLUMNS_NAME = "auto_fit_columns";AUTO_FIT_COLUMNS_DESC = "Automatically fits column width to content. Args: sheet_name (str), start_column (1-based), end_column (1-based). Example: auto_fit_columns('Sheet1', 1, 5)"

    SET_FORMULA_NAME="set_formula_in_cell"; SET_FORMULA_DESC="Sets a formula in a specific cell. Args: sheet_name (str), cell_addr (e.g., 'A1'), formula (str, e.g., '=SUM(B1:B10)'). Example: set_formula_in_cell('Sheet1', 'C1', '=A1+B1')"
    GET_FORMULA_NAME="get_formula_from_cell"; GET_FORMULA_DESC="Retrieves the formula from a cell. Args: sheet_name (str), cell_addr (e.g., 'A1'). Example: get_formula_from_cell('Sheet1', 'C1')"
    EVALUATE_FORMULA_NAME="evaluate_formula"; EVALUATE_FORMULA_DESC="Returns the computed value of a formula cell. Args: sheet_name (str), cell_addr (e.g., 'A1'). Example: evaluate_formula('Sheet1', 'C1')"

    CREATE_CHART_NAME="create_chart"; CREATE_CHART_DESC="Creates a chart. Args: sheet_name (str), chart_type (COLUMN/LINE/PIE/etc), domain_range (e.g., 'A1:A5'), data_ranges (e.g., 'B1:B5'), chart_title (str), anchor_cell (e.g., 'D1'). Example: create_chart('Sheet1', 'PIE', 'A1:A5', 'B1:B5', 'Sales')"
    UPDATE_CHART_NAME="update_chart"; UPDATE_CHART_DESC="Updates a chart. Args: sheet_name (str), chart_name (str), updates (JSON string with title/chart_type/anchor_cell). Example: update_chart('Sheet1', 'Sales', '{\"title\": \"Revenue\"}')"
    DELETE_CHART_NAME="delete_chart"; DELETE_CHART_DESC="Deletes a chart using its title. Args: sheet_name (str), chart_name (str). Example: delete_chart('Sheet1', 'Revenue')"

    GET_SHEET_METADATA="get_sheet_metadata";GET_SHEET_METADATA_DESC="Returns metadata about the spreadsheet and worksheets. No arguments required."

    SORT_RANGE_NAME="sort_range"; SORT_RANGE_DESC="Sorts data in a range. Args: sheet_name (str), start (e.g., 'A1'), end (e.g., 'C10'), sort_columns (1-based int), ascending (bool). Example: sort_range('Sheet1', 'A2', 'C10', 1, True)"
    FILTER_DATA_NAME="filter_data"; FILTER_DATA_DESC="Applies filters to a range. Args: sheet_name (str), start (e.g., 'A1'), end (e.g., 'C10'), filter_criteria (JSON string). Example: filter_data('Sheet1', 'A1', 'C10', '{\"1\": {\"hidden_values\": [\"x\"]}}')"
    REMOVE_DUPLICATES_NAME="remove_duplicates"; REMOVE_DUPLICATES_DESC="Removes duplicate rows. Args: sheet_name (str), subset_columns (list of 1-based ints). Example: remove_duplicates('Sheet1', [1, 2])"
    FIND_VALUE_NAME="find_value"; FIND_VALUE_DESC="Searches for a value. Args: sheet_name (str), search_value (str), rows (optional tuple), cols (optional tuple). Example: find_value('Sheet1', 'Target')"
    GET_UNIQUE_VALUES_NAME="get_unique_values"; GET_UNIQUE_VALUES_DESC="Returns unique values from a column. Args: sheet_name (str), column (1-based index). Example: get_unique_values('Sheet1', 1)"
    PIVOT_TABLE_CREATE_NAME="pivot_table_create"; PIVOT_TABLE_CREATE_DESC="Creates a pivot table. Args: source_sheet_name (str), target_sheet_name (str), index_col (str), value_col (str), agg_func (str), columns_col (optional str). Example: create_gsheet_pivot('Source', 'Pivot', 'Category', 'Amount', 'SUM')"
    CREATE_PIVOT_NAME="create_gsheet_pivot"
    CREATE_PIVOT_DESC="Creates a pivot table using Pandas-style logic. (Internal tool name for create_gsheet_pivot)"

    SELECT_SHEET="select_sheet";SELECT_SHEET_DESC="Selects or activates a worksheet by name. Args: sheet_name (str). Example: select_sheet('Sheet2')"
    ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE = range(10)