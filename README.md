# Google Sheets MCP SERVER 🚀

A powerful, comprehensive Model Context Protocol (MCP) server that enables AI agents to interact directly with Google Sheets. Perform everything from simple cell updates to complex data analysis and visualization using natural language.

---

## 📂 Project Structure

The project is organized into modular service layers for easy maintenance and extensibility:

- **`constants/`**: Centralized configuration and LLM-optimized tool descriptions.
  - `constants.py`: Definitions for tool names, descriptions, and GSheet keys.
- **`services/`**: Core logic for interacting with external APIs and services.
- **`tools/`**: Implementation of various spreadsheet features:
  - `data_analysis/`: Sorting, filtering, pivot tables, and unique value extraction.
  - `data_operations/`: Reading ranges, batch updates, and row/column data entry.
  - `formattings/`: Text styling, colors, alignment, borders, and number formats.
  - `formulas/`: Formula insertion and evaluation.
  - `rows_and_coloumns_operations/`: Structural changes (insert/delete/hide/show).
  - `sheet_operations/`: Sheet management (create, delete, rename, list).
  - `visualizations/`: Dynamic chart creation and updates.
- **`utils/`**: Helper utilities for color normalization and worksheet retrieval.
- **`main.py` & `server.py`**: MCP server entry points and initialization.

---

## ⚙️ Getting Started

### 1. Prerequisites

- Google Cloud Project with Google Sheets and Drive APIs enabled.
- Service account JSON credentials file placed in `assets/`.
- Python 3.10+ installed.

## Step 2: Create Google Cloud Project
- Go to **Google Cloud Console**
- Create a new project

## Step 3: Enable APIs
Enable:
- Google Sheets API
- Google Drive API

## Step 4: Create Service Account
- Go to **APIs & Services → Credentials**
- Create a Service Account

## Step 5: Create Service Account Key
- Open the Service Account
- Create a **JSON** key
- Download the file (e.g. `credentials.json`)

## Step 6: Share Google Sheet
- Open the Google Sheet
- Share it with the **service account email**
- Give **Editor** access

## Step 7: Authorize in Python
```
mount your credential to assets/ if you running through docker
set SERVICE_FILE_PATH=path to your credential if running locally

```

### 2. Verify Connection

1. **Verify Server is Running**:
   ```bash
   python main.py
   ```
2. **Cursor Configuration**:
   - Open Cursor Settings → **Developer** → **Edit Config**.
   - Ensure the server is listed (default name: `sheets-cello`).
3. **Credentials**:
   - Ensure the `SERVICE_FILE_PATH` in `constants/constants.py` or as an environment variable points to your service account JSON.

---

## 🛠️ Exhaustive Tool Reference

The agent provides **46 specialized tools** organized into the following categories. Each tool is optimized for LLM use with detailed descriptions and usage examples.

### 🔌 **Connection & Scope** (1 tool)

- `select_sheet`: Selects or activates a different Google Sheet workbook by name.

### 📊 **Data Operations** (8 tools)

- `read_range`: Retrieves values from a specific rectangular range (e.g., A1:C10).
- `read_batch_ranges`: Retrieves values from multiple non-contiguous ranges in one call.
- `read_sheet`: Fetches every single populated row and column from the worksheet.
- `get_cell_value`: Retrieves the value of a single specific cell.
- `set_cell_value`: Updates the value of a single specific cell.
- `update_row_by_index`: Updates an entire row with new data based on the row number.
- `update_or_insert_column`: Updates or inserts values into a specific column.
- `append_data_batch_in_rows`: Appends multiple rows of data, automatically finding the end if needed.
- `clear_range`: Deletes all content within a specified range of cells.

### 📑 **Sheet Management** (4 tools)

- `list_sheets`: Retrieves a list of all worksheet titles in the current spreadsheet.
- `create_sheet`: Creates a new worksheet with optional row/column size.
- `delete_sheet`: Deletes an existing worksheet by its name.
- `rename_sheet`: Updates the title of an existing worksheet.

### 🎨 **Formatting & Styling** (12 tools)

- `set_text_style`: Sets bold, italic, and font size for a range.
- `set_text_color`: Sets the foreground color of cells using RGB values.
- `set_background_color`: Sets the background (fill) color of cells using RGB values.
- `set_alignment`: Sets horizontal and/or vertical alignment of text.
- `set_wrap`: Controls how text wraps (WRAP, CLIP, OVERFLOW).
- `set_borders`: Applies borders (top, bottom, left, right) around a range.
- `set_rotation`: Rotates the text inside cells by a given angle.
- `set_number_format`: Sets number, date, currency, or percent format patterns.
- `merge_cells`: Merges all cells in a range into a single cell.
- `set_column_width`: Sets the width of a specific column in pixels.
- `set_row_height`: Sets the height of a specific row in pixels.
- `auto_fit_columns`: Automatically adjusts column widths based on content.

### 📐 **Row & Column Operations** (8 tools)

- `insert_rows`: Inserts new empty rows at a specific index.
- `delete_rows`: Deletes a specified number of rows from an index.
- `insert_columns`: Inserts new empty columns at a specific index.
- `delete_columns`: Deletes a specified number of columns from an index.
- `hide_rows`: Hides specific rows from view.
- `show_rows`: Unhides previously hidden rows.
- `hide_columns`: Hides specific columns from view.
- `show_columns`: Unhides previously hidden columns.

### 🔢 **Formulas** (3 tools)

- `set_formula_in_cell`: Inserts a Google Sheets formula (e.g., `=SUM(A1:A10)`).
- `get_formula_from_cell`: Retrieves the raw formula string from a cell.
- `evaluate_formula`: Returns the computed numeric or text result of a formula.

### 📈 **Data Analysis** (6 tools)

- `sort_range`: Sorts a range by a column in ascending or descending order.
- `filter_data`: Applies complex filtering criteria to a range.
- `remove_duplicates`: Removes duplicate rows based on specific columns.
- `find_value`: Searches for a specific value across a range or entire sheet.
- `get_unique_values`: Returns all unique values from a specific column.
- `create_gsheet_pivot`: Creates a pivot table summary on a target sheet.

### 📊 **Visualizations** (3 tools)

- `create_chart`: Creates line, bar, pie, or column charts.
- `update_chart`: Updates an existing chart's title, type, or position.
- `delete_chart`: Removes a chart from the worksheet by its title.

---

## 🔧 Troubleshooting

- **MCP Tools Not Appearing?**
  1. Ensure `python main.py` is running.
  2. Restart Cursor completely to refresh tool discovery.
- **Permission Denied?**
  - Ensure you have shared your Google Sheet with the **Service Account Email** found in your JSON credentials file.

---

#ENVIRONMENT VARIBALES

```
SERVICE_FILE_PATH= path to your credentials.json
transport= (sse,stdio,http)
mcp_host= ip to host mcp
mcp_port= port to run mcp server

```
### **Total Active Tools: 46** 🛠️
