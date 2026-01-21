# Excel MCP Server - Tools Documentation

A comprehensive Model Context Protocol (MCP) server for Excel operations, providing AI assistants with powerful spreadsheet manipulation capabilities.

## 📋 Table of Contents

- [Overview](#overview)
- [Available Tools](#available-tools)
  - [Core Data Operations](#core-data-operations)
  - [Sheet Management](#sheet-management)
  - [Formatting Tools](#formatting-tools)
  - [Formula & Calculation](#formula--calculation)
  - [Data Analysis](#data-analysis)
  - [Styling & Conditional Formatting](#styling--conditional-formatting)
  - [Chart & Visualization](#chart--visualization)
  - [Row & Column Operations](#row--column-operations)
  - [Data Import/Export](#data-importexport)
  - [Advanced Features](#advanced-features)
  - [Metadata & Info](#metadata--info)
  - [Utility Functions](#utility-functions)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage Examples](#usage-examples)

## 🎯 Overview

This MCP server enables AI assistants to interact with Excel spreadsheets through a rich set of tools. It supports reading, writing, formatting, analyzing, and visualizing data in Excel workbooks.

## 🛠️ Available Tools

### Core Data Operations

Essential operations for reading and writing data to Excel sheets.

| Tool | Description | Parameters |
|------|-------------|------------|
| `read_range` | Read data from a specific cell range | `sheet_name`, `range` (e.g., "A1:C10") |
| `write_range` | Write data to a specific cell range | `sheet_name`, `range`, `data` (2D array) |
| `read_sheet` | Read entire worksheet data | `sheet_name` |
| `get_cell_value` | Get value from a single cell | `sheet_name`, `cell` (e.g., "A1") |
| `set_cell_value` | Set value in a single cell | `sheet_name`, `cell`, `value` |
| `clear_range` | Clear contents from a range | `sheet_name`, `range` |

### Sheet Management

Tools for managing worksheets within a workbook.

| Tool | Description | Parameters |
|------|-------------|------------|
| `list_sheets` | List all worksheets in the workbook | None |
| `create_sheet` | Create a new worksheet | `sheet_name` |
| `delete_sheet` | Delete a worksheet | `sheet_name` |
| `rename_sheet` | Rename a worksheet | `old_name`, `new_name` |
### Formatting Tools

Apply visual formatting to cells and ranges.

| Tool | Description | Parameters |
|------|-------------|------------|
| `set_cell_format` | Apply formatting (bold, italic, color, etc.) | `sheet_name`, `range`, `format_options` |
| `set_number_format` | Set number/date/currency formats | `sheet_name`, `range`, `format_string` |
| `merge_cells` | Merge a range of cells | `sheet_name`, `range` |
| `unmerge_cells` | Unmerge cells | `sheet_name`, `range` |
| `set_column_width` | Adjust column width | `sheet_name`, `column`, `width` |
| `set_row_height` | Adjust row height | `sheet_name`, `row`, `height` |
| `auto_fit_columns` | Auto-fit column widths to content | `sheet_name`, `columns` |

### Formula & Calculation

Work with Excel formulas and calculations.

| Tool | Description | Parameters |
|------|-------------|------------|
| `set_formula` | Insert formula in a cell | `sheet_name`, `cell`, `formula` |
| `calculate_workbook` | Force recalculation | None |
| `get_formula` | Retrieve formula from a cell | `sheet_name`, `cell` |
| `evaluate_formula` | Evaluate a formula and return result | `sheet_name`, `formula` |

### Data Analysis

Powerful tools for analyzing and manipulating data.

| Tool | Description | Parameters |
|------|-------------|------------|
| `sort_range` | Sort data by column(s) | `sheet_name`, `range`, `sort_columns`, `ascending` |
| `filter_data` | Apply filters to data | `sheet_name`, `range`, `filter_criteria` |
| `remove_duplicates` | Remove duplicate rows | `sheet_name`, `range`, `columns` |
| `find_value` | Search for specific values | `sheet_name`, `search_value`, `range` |
| `get_unique_values` | Get unique values from a column | `sheet_name`, `column` |
| `pivot_table_create` | Create a pivot table | `sheet_name`, `source_range`, `destination`, `config` |

### Styling & Conditional Formatting

Advanced styling and conditional formatting options.

| Tool | Description | Parameters |
|------|-------------|------------|
| `set_cell_style` | Apply predefined styles | `sheet_name`, `range`, `style_name` |
| `add_conditional_format` | Add conditional formatting rules | `sheet_name`, `range`, `rule_type`, `rule_config` |
| `set_border` | Add borders to cells | `sheet_name`, `range`, `border_style` |
| `set_background_color` | Set cell background color | `sheet_name`, `range`, `color` |
| `set_font_color` | Set text color | `sheet_name`, `range`, `color` |

### Chart & Visualization

Create and manage charts in Excel.

| Tool | Description | Parameters |
|------|-------------|------------|
| `create_chart` | Create charts (line, bar, pie, etc.) | `sheet_name`, `chart_type`, `data_range`, `chart_config` |
| `update_chart` | Modify existing chart | `sheet_name`, `chart_id`, `updates` |
| `delete_chart` | Remove a chart | `sheet_name`, `chart_id` |

### Row & Column Operations

Manipulate rows and columns in worksheets.

| Tool | Description | Parameters |
|------|-------------|------------|
| `insert_rows` | Insert new rows | `sheet_name`, `row_index`, `count` |
| `delete_rows` | Delete rows | `sheet_name`, `row_index`, `count` |
| `insert_columns` | Insert new columns | `sheet_name`, `column_index`, `count` |
| `delete_columns` | Delete columns | `sheet_name`, `column_index`, `count` |
| `hide_rows` | Hide specific rows | `sheet_name`, `row_indices` |
| `show_rows` | Unhide rows | `sheet_name`, `row_indices` |
| `hide_columns` | Hide specific columns | `sheet_name`, `column_indices` |
| `show_columns` | Unhide columns | `sheet_name`, `column_indices` |

### Data Import/Export

Import and export data in various formats.

| Tool | Description | Parameters |
|------|-------------|------------|
| `import_csv` | Import CSV data into sheet | `sheet_name`, `csv_data` or `file_path` |
| `export_csv` | Export sheet data to CSV | `sheet_name`, `range`, `file_path` |
| `import_json` | Import JSON data | `sheet_name`, `json_data`, `mapping` |
| `export_json` | Export data as JSON | `sheet_name`, `range` |

### Advanced Features

Advanced Excel features for power users.

| Tool | Description | Parameters |
|------|-------------|------------|
| `protect_sheet` | Add sheet protection | `sheet_name`, `password` (optional) |
| `unprotect_sheet` | Remove sheet protection | `sheet_name`, `password` |
| `add_data_validation` | Add dropdown lists or validation rules | `sheet_name`, `range`, `validation_type`, `criteria` |
| `freeze_panes` | Freeze rows/columns | `sheet_name`, `row`, `column` |
| `unfreeze_panes` | Unfreeze panes | `sheet_name` |
| `add_comment` | Add comment to cell | `sheet_name`, `cell`, `comment_text` |
| `get_named_range` | Get data from named range | `range_name` |
| `create_named_range` | Define a named range | `range_name`, `sheet_name`, `range` |

### Metadata & Info

Retrieve information about workbooks and sheets.

| Tool | Description | Parameters |
|------|-------------|------------|
| `get_workbook_info` | Get workbook metadata | None |
| `get_sheet_dimensions` | Get used range dimensions (rows/columns) | `sheet_name` |
| `get_last_row` | Find last row with data | `sheet_name`, `column` |
| `get_last_column` | Find last column with data | `sheet_name`, `row` |

### Utility Functions

Helpful utility functions for common operations.

| Tool | Description | Parameters |
|------|-------------|------------|
| `search_and_replace` | Find and replace text | `sheet_name`, `search_text`, `replace_text`, `range` |
| `copy_range` | Copy data from one range to another | `sheet_name`, `source_range`, `destination_cell` |
| `paste_values` | Paste values only (no formulas) | `sheet_name`, `source_range`, `destination_cell` |
| `transpose_range` | Transpose rows to columns | `sheet_name`, `source_range`, `destination_cell` |
| `concatenate_columns` | Combine multiple columns | `sheet_name`, `columns`, `separator`, `destination_column` |

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/your-org/excel-mcp-server.git

# Install dependencies
cd excel-mcp-server
npm install

# Build the server
npm run build
```

## ⚙️ Configuration

Add the Excel MCP server to your MCP settings configuration:

```json
{
  "mcpServers": {
    "excel": {
      "command": "node",
      "args": ["/path/to/excel-mcp-server/build/index.js"],
      "env": {
        "EXCEL_WORKBOOK_PATH": "/path/to/your/workbook.xlsx"
      }
    }
  }
}
```

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `EXCEL_WORKBOOK_PATH` | Path to the Excel workbook | Yes |
| `EXCEL_AUTO_SAVE` | Auto-save changes (true/false) | No (default: true) |
| `EXCEL_READ_ONLY` | Open in read-only mode | No (default: false) |

## 💡 Usage Examples

### Example 1: Reading and Writing Data

```javascript
// Read data from a range
const data = await read_range({
  sheet_name: "Sheet1",
  range: "A1:C10"
});

// Write data to a range
await write_range({
  sheet_name: "Sheet1",
  range: "A1:C3",
  data: [
    ["Name", "Age", "City"],
    ["Alice", 30, "New York"],
    ["Bob", 25, "San Francisco"]
  ]
});
```

### Example 2: Creating a Chart

```javascript
await create_chart({
  sheet_name: "Sheet1",
  chart_type: "column",
  data_range: "A1:B10",
  chart_config: {
    title: "Sales by Month",
    x_axis_title: "Month",
    y_axis_title: "Sales ($)"
  }
});
```

### Example 3: Data Analysis

```javascript
// Sort data
await sort_range({
  sheet_name: "Sheet1",
  range: "A1:C100",
  sort_columns: [{ column: "B", ascending: false }]
});

// Get unique values
const uniqueValues = await get_unique_values({
  sheet_name: "Sheet1",
  column: "C"
});
```

### Example 4: Formatting

```javascript
// Apply formatting
await set_cell_format({
  sheet_name: "Sheet1",
  range: "A1:C1",
  format_options: {
    bold: true,
    font_size: 14,
    background_color: "#4472C4",
    font_color: "#FFFFFF"
  }
});
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🐛 Issues & Support

For issues, questions, or suggestions, please open an issue on GitHub.

## 🔗 Related Resources

- [MCP Documentation](https://modelcontextprotocol.io)
- [Excel API Reference](https://docs.microsoft.com/en-us/office/dev/add-ins/reference/overview/excel-add-ins-reference-overview)

---

Made with ❤️ for the MCP community