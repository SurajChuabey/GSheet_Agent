# How to Use Your Google Sheets MCP Server in Cursor

## ✅ Step 1: Verify Connection

1. **Restart Cursor** (if you haven't already)
   - Close Cursor completely
   - Reopen it

2. **Check MCP Tools**:
   - Open Cursor Settings → **Developer** → **Edit Config**
   - Select **MCP Tools**
   - You should see **"sheets-cello"** listed

3. **Verify Server is Running**:
   ```bash
   # Make sure your MCP server is running
   python main.py
   ```

## 🚀 Step 2: Using MCP Tools in Cursor Chat

Once connected, you can use natural language in Cursor's chat to interact with Google Sheets. The AI will automatically use the appropriate MCP tools.

### Example Conversations:

#### **Reading Data:**
```
"Read the data from cells A1 to C10 in my sheet"
"Get the value from cell B5"
"Show me all the data in Sheet1"
```

#### **Writing Data:**
```
"Set cell A1 to 'Hello World'"
"Update row 3 with values: John, 25, Developer"
"Add these rows starting at A10: Alice,30,Engineer;Bob,28,Designer"
```

#### **Sheet Management:**
```
"List all sheets in my spreadsheet"
"Create a new sheet called 'Sales Data'"
"Rename Sheet1 to 'January Data'"
"Delete the sheet named 'Old Data'"
```

#### **Formatting:**
```
"Make cell A1 bold and red"
"Set background color of range A1:C5 to yellow"
"Center align the text in column B"
"Merge cells A1 to C1"
```

#### **Data Analysis:**
```
"Sort the data in range A1:C100 by column B in descending order"
"Find all rows containing 'John' in column A"
"Remove duplicate rows from range A1:C50"
"Get unique values from column C"
```

#### **Charts:**
```
"Create a bar chart for data in range A1:B10"
"Create a pie chart showing sales data from A1:B5"
```

## 📋 Available MCP Tools

Your server provides **47+ tools** organized into categories:

### 📊 **Data Operations** (9 tools)
- `read_range` - Read data from a range (e.g., A1:C10)
- `read_batch_ranges` - Read multiple ranges at once
- `read_sheet` - Read entire sheet
- `get_cell_value` - Get single cell value
- `set_cell_value` - Set single cell value
- `update_row_by_index` - Update entire row
- `update_or_insert_column` - Update column
- `append_data_batch_in_rows` - Add multiple rows
- `clear_range` - Clear cell range

### 📑 **Sheet Operations** (4 tools)
- `list_sheets` - List all sheets
- `create_sheet` - Create new sheet
- `delete_sheet` - Delete sheet
- `rename_sheet` - Rename sheet
- `select_sheet` - Switch to different Google Sheet workbook

### 🎨 **Formatting** (12 tools)
- `set_text_style` - Bold, italic, font size
- `set_text_color` - Text color (RGB)
- `set_background_color` - Background color (RGB)
- `set_alignment` - Horizontal/vertical alignment
- `set_wrap` - Text wrapping
- `set_borders` - Cell borders
- `set_rotation` - Text rotation
- `set_number_format` - Number/date/currency format
- `merge_cells` - Merge cell range
- `set_column_width` - Set column width
- `set_row_height` - Set row height
- `auto_fit_columns` - Auto-fit column width

### 📐 **Row & Column Operations** (8 tools)
- `insert_rows` - Insert rows
- `delete_rows` - Delete rows
- `insert_columns` - Insert columns
- `delete_columns` - Delete columns
- `hide_rows` - Hide rows
- `show_rows` - Show hidden rows
- `hide_columns` - Hide columns
- `show_columns` - Show hidden columns

### 🔢 **Formulas** (3 tools)
- `set_formula_in_cell` - Set formula in cell
- `get_formula_from_cell` - Get formula from cell
- `evaluate_formula` - Evaluate formula value

### 📈 **Data Analysis** (6 tools)
- `sort_range` - Sort data by columns
- `filter_data` - Apply filters
- `remove_duplicates` - Remove duplicate rows
- `find_value` - Search for values
- `get_unique_values` - Get unique values
- `create_gsheet_pivot` - Create pivot table

### 📊 **Visualizations** (3 tools)
- `create_chart` - Create charts (bar, line, pie, etc.)
- `update_chart` - Update existing chart
- `delete_chart` - Delete chart

### ℹ️ **Metadata** (1 tool)
- `get_sheet_metadata` - Get full sheet information

## 💡 Tips for Best Results

1. **Be Specific**: Mention sheet names, cell ranges, and exact values
   - ✅ Good: "Read range A1:C10 from Sheet1"
   - ❌ Vague: "Read some data"

2. **Use Natural Language**: The AI understands conversational requests
   - ✅ "Add a new row with my name, age, and city"
   - ✅ "Make the header row bold and blue"
   - ✅ "Create a chart showing sales by month"

3. **First Read, Then Write**: For complex operations, the AI will first read the sheet to understand the structure

4. **Sheet Selection**: If working with multiple Google Sheet workbooks, use `select_sheet` first:
   - "Switch to the sheet named 'Sales Report'"
   - "Select the 'book' spreadsheet"

## 🔧 Troubleshooting

### MCP Tools Not Appearing?
1. Verify server is running: `python main.py`
2. Check `.cursor/mcp.json` exists and has correct URL
3. Restart Cursor completely
4. Check server logs for errors

### Connection Issues?
1. Verify server is accessible at `http://localhost:9001/sse`
2. Check firewall settings
3. For remote servers, update URL in `mcp.json` to use IP address

### Tools Not Working?
1. Ensure Google Sheets API credentials are set up correctly
2. Check that the service account has access to your sheets
3. Verify the sheet name exists in your Google Drive

## 🎯 Quick Start Examples

### Example 1: Basic Data Entry
```
You: "Add a header row in Sheet1 with: Name, Age, City, Salary"
AI: [Uses set_cell_value or append_data_batch_in_rows]

You: "Add a row with: Alice, 30, New York, 75000"
AI: [Uses append_data_batch_in_rows]
```

### Example 2: Data Analysis
```
You: "Read all data from Sheet1"
AI: [Uses read_sheet]

You: "Sort the data by the Salary column in descending order"
AI: [Uses sort_range]
```

### Example 3: Formatting
```
You: "Make the first row bold with blue background"
AI: [Uses set_text_style and set_background_color]

You: "Center align all headers"
AI: [Uses set_alignment]
```

### Example 4: Charts
```
You: "Create a bar chart for the data in A1:B10 showing sales by month"
AI: [Uses create_chart with appropriate configuration]
```

---

**Happy Spreadsheet Automation! 🎉**
