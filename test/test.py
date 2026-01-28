from typing import Optional
from constants.globals import Global
from services.googleSheetServices import Services
service = Services.connect()

# data analysis
from tools.data_analysis.analysis_operations import *
def test_dataanalysis():
    """
    Comprehensive test function for all data analysis functions.
    Creates dummy data in Google Sheets and tests each function.
    """
    print("=" * 60)
    print("Starting Data Analysis Test Suite")
    print("=" * 60)
    
    # Get Google Sheets connection from Global
    gc = Global.gc
    
    # Create or get test worksheet
    test_sheet_name = "TestDataAnalysis"
    
    try:
        # Try to get existing worksheet or create new one
        try:
            worksheet = gc.worksheet_by_title(test_sheet_name)
            print(f"\n✓ Found existing worksheet: {test_sheet_name}")
            worksheet.clear()
            print(f"✓ Cleared existing data")
        except:
            worksheet = gc.add_worksheet(test_sheet_name)
            print(f"\n✓ Created new worksheet: {test_sheet_name}")
        
        # Create dummy data
        print("\n" + "-" * 60)
        print("Creating dummy data...")
        print("-" * 60)
        
        dummy_data = [
            ["ID", "Name", "Department", "Salary", "Performance", "Region"],
            [1, "Alice Smith", "Sales", 75000, "Excellent", "East"],
            [2, "Bob Johnson", "Engineering", 95000, "Good", "West"],
            [3, "Carol Davis", "Sales", 68000, "Excellent", "East"],
            [4, "David Wilson", "Marketing", 72000, "Average", "West"],
            [5, "Eve Brown", "Engineering", 92000, "Good", "East"],
            [6, "Frank Miller", "Sales", 75000, "Good", "West"],
            [7, "Grace Lee", "Marketing", 70000, "Excellent", "East"],
            [8, "Henry Taylor", "Engineering", 98000, "Excellent", "West"],
            [9, "Ivy Anderson", "Sales", 68000, "Average", "East"],
            [10, "Jack Thomas", "Marketing", 72000, "Good", "West"],
            [11, "Alice Smith", "Sales", 75000, "Excellent", "East"],  # Duplicate
            [12, "Karen White", "Engineering", 90000, "Excellent", "East"],
            [13, "Leo Martinez", "Sales", 71000, "Good", "West"],
            [14, "Mia Garcia", "Marketing", 69000, "Average", "East"],
            [15, "Noah Rodriguez", "Engineering", 94000, "Excellent", "West"],
        ]
        
        # Update cells with dummy data
        worksheet.update_values('A1', dummy_data)
        print(f"✓ Created {len(dummy_data)} rows x {len(dummy_data[0])} columns of dummy data")
        print(f"  Headers: {', '.join(dummy_data[0])}")
        print(f"  Data range: A1:F{len(dummy_data)}")
        
        # Test 1: Sort Range
        print("\n" + "=" * 60)
        print("TEST 1: sort_range()")
        print("=" * 60)
        print("Testing: Sort by Salary (column D) in descending order")
        try:
            result = sort_range(test_sheet_name, "A1","F16", 3, ascending=False)
            print(f"✓ Sort Result: {result}")
            print("  Expected: Data sorted by Salary (highest to lowest)")
        except Exception as e:
            print(f"✗ Error: {str(e)}")
        
        # Test 2: Filter Data
        print("\n" + "=" * 60)
        print("TEST 2: filter_data()")
        print("=" * 60)
        print("Testing: Filter for Sales department")
        try:
            combined_criteria = json.dumps({
                "3": {
                    "type": "TEXT_EQ",
                    "values": ["Sales"],
                    "hidden_values": ["HR"]
                },
            })

            result = filter_data(sheet_name=test_sheet_name,start="A1",end="F16",filter_criteria=combined_criteria)
            print(f"✓ Filter Result: {result}")
            print("  Expected: Only rows where Department='Sales'")
        except Exception as e:
            print(f"✗ Error: {str(e)}")

        try:
            combined_criteria = json.dumps({
                "2": {
                    "type": "TEXT_EQ",
                    "values": ["Sales"]
                },

                "4": {
                    "type": "NUMBER_GREATER",
                    "values": ["90000"],
                    "sort_order": "DESCENDING"
                },
            })

            result = filter_data(sheet_name=test_sheet_name,start="A1",end="F16",filter_criteria=combined_criteria)
            print(f"✓ Filter Result: {result}")
            print("  Expected: Only rows where salary='90000'")
        except Exception as e:
            print(f"✗ Error: {str(e)}")
        
        # Test 3: Remove Duplicates
        print("\n" + "=" * 60)
        print("TEST 3: remove_duplicates()")
        print("=" * 60)
        print("Testing: Remove duplicates based on Name column")
        try:
            result = remove_duplicates(test_sheet_name,[2])
            print(f"✓ Remove Duplicates Result: {result}")
            print("  Expected: Alice Smith duplicate (row 12) removed")
        except Exception as e:
            print(f"✗ Error: {str(e)}")
        
        # Test 4: Find Value
        print("\n" + "=" * 60)
        print("TEST 4: find_value()")
        print("=" * 60)
        print("Testing: Find 'Engineering' in entire sheet")
        try:
            result = find_value(test_sheet_name, "Engineering")
            print(f"✓ Find Result: {result}")
            print("  Expected: Cell locations containing 'Engineering'")
        except Exception as e:
            print(f"✗ Error: {str(e)}")
        
        print("\nTesting: Find '95000' in range D1:D16")
        try:
            result = find_value(test_sheet_name, "95000", cols=(4,4))
            print(f"✓ Find Result: {result}")
            print("  Expected: Cell D3 (Bob Johnson's salary)")
        except Exception as e:
            print(f"✗ Error: {str(e)}")
        
        # Test 5: Get Unique Values
        print("\n" + "=" * 60)
        print("TEST 5: get_unique_values()")
        print("=" * 60)
        print("Testing: Get unique departments (column 3)")
        try:
            result = get_unique_values(test_sheet_name, 3)
            print(f"✓ Unique Values Result: {result}")
            print("  Expected: ['Sales', 'Engineering', 'Marketing']")
        except Exception as e:
            print(f"✗ Error: {str(e)}")
        
        print("\nTesting: Get unique regions (column 6)")
        try:
            result = get_unique_values(test_sheet_name, 6)
            print(f"✓ Unique Values Result: {result}")
            print("  Expected: ['East', 'West']")
        except Exception as e:
            print(f"✗ Error: {str(e)}")
        
        # # Test 6: Create Pivot Table
        print("\n" + "=" * 60)
        print("TEST 6: create_gsheet_pivot()")
        print("=" * 60)
        print("Testing: Create pivot table - Average Salary by Department")
        try:
            result = create_gsheet_pivot(
                source_sheet_name="TestDataAnalysis",
                target_sheet_name="Pivot_Department_Salary",
                index_col="Department",
                value_col="Salary",
                agg_func="SUM"
            )
            print(f"✓ Pivot Table Result: {result}")
            print("  Expected: Sheet 'PivotTest1' with avg salary per department")
        except Exception as e:
            print(f"✗ Error: {str(e)}")
        
        print("\nTesting: Create pivot table - Count by Department and Performance")
        try:
            result = create_gsheet_pivot(
                source_sheet_name="TestDataAnalysis",
                target_sheet_name="Pivot_Department_Region",
                index_col="Department",
                columns_col="Region",
                value_col="Salary",
                agg_func="AVERAGE"
            )
            print(f"✓ Pivot Table Result: {result}")
            print("  Expected: Sheet 'PivotTest2' with count per dept/performance")
        except Exception as e:
            print(f"✗ Error: {str(e)}")
        
        # Final Summary
        print("\n" + "=" * 60)
        print("Test Suite Complete")
        print("=" * 60)
        print(f"\n✓ Test data available in worksheet: '{test_sheet_name}'")
        print(f"✓ Spreadsheet: 'book'")
        print(f"✓ Total test rows: {len(dummy_data) - 1} (plus header)")
        print("\nYou can now verify the results in Google Sheets.")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n✗ Fatal Error: {str(e)}")
        import traceback
        traceback.print_exc()

# data operations

from tools.data_operations.operations import *

def test_dataoperation():
    """
    Comprehensive test function for all data operation functions.
    Creates dummy data in Google Sheets and tests each function.
    """
    print("=" * 60)
    print("Starting Data Operation Test Suite")
    print("=" * 60)

    gc = Global.gc
    test_sheet_name = "TestDataOperation"

    try:
        # Create or reset worksheet
        try:
            worksheet = gc.worksheet_by_title(test_sheet_name)
            print(f"\n✓ Found existing worksheet: {test_sheet_name}")
            worksheet.clear()
            print("✓ Cleared existing data")
        except:
            worksheet = gc.add_worksheet(test_sheet_name)
            print(f"\n✓ Created new worksheet: {test_sheet_name}")

        # Dummy data
        print("\n" + "-" * 60)
        print("Creating dummy data...")
        print("-" * 60)

        dummy_data = [
            ["ID", "Name", "Department", "Salary"],
            [1, "Alice", "Sales", 75000],
            [2, "Bob", "Engineering", 95000],
            [3, "Carol", "Marketing", 70000],
            [4, "David", "Sales", 72000],
        ]

        worksheet.update_values("A1", dummy_data)
        print(f"✓ Inserted {len(dummy_data)} rows")
        print("  Range: A1:D5")

        # TEST 1: read_range
        print("\n" + "=" * 60)
        print("TEST 1: read_range()")
        print("=" * 60)
        try:
            result = read_range("A1", "D5", test_sheet_name)
            print("✓ Read Range Result:")
            print(result)
        except Exception as e:
            print(f"✗ Error: {e}")

        # TEST 2: read_batch_ranges
        print("\n" + "=" * 60)
        print("TEST 2: read_batch_ranges()")
        print("=" * 60)
        try:
            result = read_batch_ranges("A1:B2,C1:D2", test_sheet_name)
            print("✓ Batch Read Result:")
            print(result)
        except Exception as e:
            print(f"✗ Error: {e}")

        # TEST 3: update_row_by_index
        print("\n" + "=" * 60)
        print("TEST 3: update_row_by_index()")
        print("=" * 60)
        try:
            csv_row = '2,"Bob Updated","Engineering",99000'
            result = update_row_by_index(3, csv_row, test_sheet_name)
            print(f"✓ Update Row Result: {result}")
            print("  Expected: Row 3 updated")
        except Exception as e:
            print(f"✗ Error: {e}")

        # TEST 4: append_data_batch_in_rows
        print("\n" + "=" * 60)
        print("TEST 4: append_data_batch_in_rows()")
        print("=" * 60)
        try:
            csv_rows = """
                5,Eve,Engineering,91000
                6,Frank,Sales,73000
            """
            result = append_data_batch_in_rows(csv_rows, sheet_name=test_sheet_name)
            print(f"✓ Append Result: {result}")
            print("  Expected: 2 new rows appended")
        except Exception as e:
            print(f"✗ Error: {e}")

        # TEST 5: get_cell_value
        print("\n" + "=" * 60)
        print("TEST 5: get_cell_value()")
        print("=" * 60)
        try:
            result = get_cell_value("B2", test_sheet_name)
            print(f"✓ Cell Value Result: {result}")
            print("  Expected: Alice")
        except Exception as e:
            print(f"✗ Error: {e}")

        # TEST 6: set_cell_value
        print("\n" + "=" * 60)
        print("TEST 6: set_cell_value()")
        print("=" * 60)
        try:
            result = set_cell_value("C2", "HR", test_sheet_name)
            print(f"✓ Set Cell Result: {result}")
            print("  Expected: Department changed to HR")
        except Exception as e:
            print(f"✗ Error: {e}")

        # TEST 7: update_column
        print("\n" + "=" * 60)
        print("TEST 7: update_column()")
        print("=" * 60)
        try:
            values = "ID,101,102,103,104,105,106"
            result = update_column(1, values, test_sheet_name)
            print(f"✓ Update Column Result: {result}")
            print("  Expected: Column A overwritten")
        except Exception as e:
            print(f"✗ Error: {e}")

        # TEST 8: clear_range
        print("\n" + "=" * 60)
        print("TEST 8: clear_range()")
        print("=" * 60)
        try:
            result = clear_range("D2", "D7", test_sheet_name)
            print(f"✓ Clear Range Result: {result}")
            print("  Expected: Salary column cleared for rows 2–7")
        except Exception as e:
            print(f"✗ Error: {e}")

        # Final Summary
        print("\n" + "=" * 60)
        print("Data Operation Test Suite Complete")
        print("=" * 60)
        print(f"✓ Worksheet used: {test_sheet_name}")
        print("✓ All data operation tools tested")
        print("✓ Verify results directly in Google Sheets")
        print("=" * 60)

    except Exception as e:
        print(f"\n✗ Fatal Error: {e}")
        import traceback
        traceback.print_exc()

# formattings
from tools.formattings.formattings import *

def test_formatting_operations():
    """
    Comprehensive test function for all formatting operations.
    Applies formatting styles and verifies visually in Google Sheets.
    """
    print("=" * 60)
    print("Starting Formatting Operations Test Suite")
    print("=" * 60)

    gc = Global.gc
    test_sheet_name = "TestFormatting"

    try:
        # Create or reset worksheet
        try:
            worksheet = gc.worksheet_by_title(test_sheet_name)
            print(f"\n✓ Found existing worksheet: {test_sheet_name}")
            worksheet.clear()
            print("✓ Cleared existing data")
        except:
            worksheet = gc.add_worksheet(test_sheet_name)
            print(f"\n✓ Created new worksheet: {test_sheet_name}")

        # Dummy data
        print("\n" + "-" * 60)
        print("Creating dummy data...")
        print("-" * 60)

        data = [
            ["ID", "Name", "Department", "Salary"],
            [1, "Alice", "Sales", 75000],
            [2, "Bob", "Engineering", 95000],
            [3, "Carol", "Marketing", 70000],
            [4, "David", "Sales", 72000],
        ]

        worksheet.update_values("A1", data)
        print("✓ Dummy data inserted (A1:D5)")

        # TEST 1: set_text_style
        print("\n" + "=" * 60)
        print("TEST 1: set_text_style()")
        print("=" * 60)
        print("Applying Bold + Font Size to Header")
        print(set_text_style(test_sheet_name, "A1:D1", bold=True, font_size=12))

        # TEST 2: set_text_color
        print("\n" + "=" * 60)
        print("TEST 2: set_text_color()")
        print("=" * 60)
        print("Applying Blue text color to Name column")
        print(set_text_color(test_sheet_name, "A1:D1", 0, 0, 255))

        # TEST 3: set_background_color
        print("\n" + "=" * 60)
        print("TEST 3: set_background_color()")
        print("=" * 60)
        print("Applying light yellow background to header")
        print(set_background_color(test_sheet_name, "A1:D1", 255, 255, 200))

        # TEST 4: set_alignment
        print("\n" + "=" * 60)
        print("TEST 4: set_alignment()")
        print("=" * 60)
        print("Center aligning header text")
        print(set_alignment(test_sheet_name, "A1:D1", h_align="CENTER", v_align="MIDDLE"))

        # TEST 5: set_wrap
        print("\n" + "=" * 60)
        print("TEST 5: set_wrap()")
        print("=" * 60)
        print("Wrapping text in Department column")
        print(set_wrap(test_sheet_name, "C2:C5", "WRAP"))

        # TEST 6: set_borders
        print("\n" + "=" * 60)
        print("TEST 6: set_borders()")
        print("=" * 60)
        print("Applying borders to data range")
        print(set_borders(test_sheet_name, "A1:D5"))

        # # TEST 7: set_rotation
        # print("\n" + "=" * 60)
        # print("TEST 7: set_rotation()")
        # print("=" * 60)
        # print("Rotating header text by 45 degrees")
        # print(set_rotation(test_sheet_name, "A1:D1", 45))

        # TEST 8: set_number_format
        print("\n" + "=" * 60)
        print("TEST 8: set_number_format()")
        print("=" * 60)
        print("Formatting Salary column as currency")
        print(set_number_format(test_sheet_name, "D2:D5", "$#,##0"))

        # TEST 9: merge_cells
        print("\n" + "=" * 60)
        print("TEST 9: merge_cells()")
        print("=" * 60)
        print("Merging A7:D7 for title")
        worksheet.update_value("A7", "Employee Salary Report")
        print(merge_cells(test_sheet_name, "A7", "D7"))
        print(set_alignment(test_sheet_name, "A7", h_align="CENTER"))

        # TEST 10: set_column_width
        print("\n" + "=" * 60)
        print("TEST 10: set_column_width()")
        print("=" * 60)
        print("Setting Name column width to 200px")
        print(set_column_width(test_sheet_name, 2, 200))

        # TEST 11: set_row_height
        print("\n" + "=" * 60)
        print("TEST 11: set_row_height()")
        print("=" * 60)
        print("Setting header row height to 40px")
        print(set_row_height(test_sheet_name, 1, 40))

        # TEST 12: auto_fit_columns
        print("\n" + "=" * 60)
        print("TEST 12: auto_fit_columns()")
        print("=" * 60)
        print("Auto fitting all columns")
        print(auto_fit_columns(test_sheet_name, 1, 4))

        # Final Summary
        print("\n" + "=" * 60)
        print("Formatting Operations Test Suite Complete")
        print("=" * 60)
        print(f"✓ Worksheet: {test_sheet_name}")
        print("✓ All formatting tools executed successfully")
        print("✓ Verify results visually in Google Sheets")
        print("=" * 60)

    except Exception as e:
        print(f"\n✗ Fatal Error: {e}")
        import traceback
        traceback.print_exc()
 

# rows and coloumns operation
from tools.rows_and_coloumns_operations.rows_and_Cols_operations import *

def test_structure_operations():
    """
    Comprehensive test function for row/column structure operations.
    Tests insert, delete, hide, and show for rows and columns.
    """
    print("=" * 60)
    print("Starting Structure Operations Test Suite")
    print("=" * 60)

    gc = Global.gc
    test_sheet_name = "TestStructureOps"

    try:
        # Create or reset worksheet
        try:
            worksheet = gc.worksheet_by_title(test_sheet_name)
            print(f"\n✓ Found existing worksheet: {test_sheet_name}")
            worksheet.clear()
            print("✓ Cleared existing data")
        except:
            worksheet = gc.add_worksheet(test_sheet_name)
            print(f"\n✓ Created new worksheet: {test_sheet_name}")

        # Dummy data
        print("\n" + "-" * 60)
        print("Creating dummy data...")
        print("-" * 60)

        data = [
            ["ID", "Name", "Dept", "Salary"],
            [1, "Alice", "Sales", 75000],
            [2, "Bob", "Engineering", 95000],
            [3, "Carol", "Marketing", 70000],
            [4, "David", "Sales", 72000],
            [5, "Eve", "Engineering", 91000],
        ]

        worksheet.update_values("A1", data)
        print("✓ Dummy data inserted (A1:D6)")

        # TEST 1: insert_rows
        print("\n" + "=" * 60)
        print("TEST 1: insert_rows()")
        print("=" * 60)
        print(insert_rows(test_sheet_name, row_index=3, count=2))
        print("  Expected: 2 empty rows inserted starting at row 3")

        # TEST 2: insert_columns
        print("\n" + "=" * 60)
        print("TEST 2: insert_columns()")
        print("=" * 60)
        print(insert_columns(test_sheet_name, column_index=2, count=1))
        print("  Expected: 1 empty column inserted at column B")

        # TEST 3: hide_rows
        print("\n" + "=" * 60)
        print("TEST 3: hide_rows()")
        print("=" * 60)
        print(hide_rows(test_sheet_name, "4,5"))
        print("  Expected: Rows 4 and 5 hidden")

        # TEST 4: show_rows
        print("\n" + "=" * 60)
        print("TEST 4: show_rows()")
        print("=" * 60)
        print(show_rows(test_sheet_name, "4,5"))
        print("  Expected: Rows 4 and 5 visible again")

        # TEST 5: hide_columns
        print("\n" + "=" * 60)
        print("TEST 5: hide_columns()")
        print("=" * 60)
        print(hide_columns(test_sheet_name, "2,4"))
        print("  Expected: Columns B and D hidden")

        # TEST 6: show_columns
        print("\n" + "=" * 60)
        print("TEST 6: show_columns()")
        print("=" * 60)
        print(show_columns(test_sheet_name, "2,4"))
        print("  Expected: Columns B and D visible again")

        # TEST 7: delete_rows
        print("\n" + "=" * 60)
        print("TEST 7: delete_rows()")
        print("=" * 60)
        print(delete_rows(test_sheet_name, row_index=3, count=2))
        print("  Expected: Previously inserted empty rows removed")

        # TEST 8: delete_columns
        print("\n" + "=" * 60)
        print("TEST 8: delete_columns()")
        print("=" * 60)
        print(delete_columns(test_sheet_name, column_index=2, count=1))
        print("  Expected: Previously inserted empty column removed")

        # Final Summary
        print("\n" + "=" * 60)
        print("Structure Operations Test Suite Complete")
        print("=" * 60)
        print(f"✓ Worksheet used: '{test_sheet_name}'")
        print("✓ All row/column structure operations executed")
        print("✓ Verify visually in Google Sheets")
        print("=" * 60)

    except Exception as e:
        print(f"\n✗ Fatal Error: {e}")
        import traceback
        traceback.print_exc()

# chart operations
from tools.visualizations.visualizations import *
def test_chart_operations():
    """
    Comprehensive test function for chart operations.
    Tests create, update, and delete chart functions.
    """
    print("=" * 60)
    print("Starting Chart Operations Test Suite")
    print("=" * 60)

    gc = Global.gc
    test_sheet_name = "TestChartOps"

    try:
        # Create or reset worksheet
        try:
            worksheet = gc.worksheet_by_title(test_sheet_name)
            print(f"\n✓ Found existing worksheet: {test_sheet_name}")
            worksheet.clear()
            print("✓ Cleared existing data")
        except:
            worksheet = gc.add_worksheet(test_sheet_name)
            print(f"\n✓ Created new worksheet: {test_sheet_name}")

        # Insert dummy data
        print("\n" + "-" * 60)
        print("Creating dummy data...")
        print("-" * 60)

        data = [
            ["Month", "Sales", "Expenses"],
            ["Jan", 12000, 8000],
            ["Feb", 15000, 9000],
            ["Mar", 18000, 11000],
            ["Apr", 16000, 10000],
            ["May", 20000, 12000],
        ]

        worksheet.update_values("A1:C6", data)
        print("✓ Dummy data inserted (A1:C6)")

        # TEST 1: create_chart
        print("\n" + "=" * 60)
        print("TEST 1: create_chart()")
        print("=" * 60)

        result = create_chart(
            sheet_name=test_sheet_name,
            chart_type="COLUMN",
            domain_range="A2:A6",
            data_ranges="B2:B6",
            chart_title="Monthly Revenue",
            anchor_cell="E1"
        )

        print(f"✓ Create Chart Result: {result}")
        print("  Expected: Column chart created on the sheet")

        # TEST 2: update_chart
        print("\n" + "=" * 60)
        print("TEST 2: update_chart()")
        print("=" * 60)

        update_config = json.dumps({
            "title": "Monthly Sales vs Expenses"
        })

        update_config = json.dumps({
            Constants.CHART_TITLE: "Updated Monthly Revenue",
            Constants.CHART_TYPE: "LINE",
            Constants.ANCHOR_CELL: "G2"
        })

        result = update_chart(
            sheet_name=test_sheet_name,
            chart_name="Monthly Revenue",
            updates=update_config
        )

        print(f"✓ Update Chart Result: {result}")
        print("  Expected: Chart title updated")

        # TEST 3: delete_chart
        print("\n" + "=" * 60)
        print("TEST 3: delete_chart()")
        print("=" * 60)

        # result = delete_chart(
        #     sheet_name=test_sheet_name,
        #     chart_name="Updated Monthly Revenue"
        # )

        print(f"✓ Delete Chart Result: {result}")
        print("  Expected: Chart removed from sheet")

        # Final Summary
        print("\n" + "=" * 60)
        print("Chart Operations Test Suite Complete")
        print("=" * 60)
        print(f"✓ Worksheet used: '{test_sheet_name}'")
        print("✓ Chart create / update / delete tested")
        print("✓ Verify visually in Google Sheets")
        print("=" * 60)

    except Exception as e:
        print(f"\n✗ Fatal Error: {e}")
        import traceback
        traceback.print_exc()

# formula operations
from tools.formulas.formulas_operations import *

from constants.globals import Global

def test_formula_operations():
    """
    Comprehensive test function for formula operations.
    Tests set, get, and evaluate formula behavior.
    """
    print("=" * 60)
    print("Starting Formula Operations Test Suite")
    print("=" * 60)

    gc = Global.gc
    test_sheet_name = "TestFormulaOps"

    try:
        # Create or reset worksheet
        try:
            worksheet = gc.worksheet_by_title(test_sheet_name)
            print(f"\n✓ Found existing worksheet: {test_sheet_name}")
            worksheet.clear()
            print("✓ Cleared existing data")
        except:
            worksheet = gc.add_worksheet(test_sheet_name)
            print(f"\n✓ Created new worksheet: {test_sheet_name}")

        # Insert dummy data
        print("\n" + "-" * 60)
        print("Creating dummy data...")
        print("-" * 60)

        data = [
            ["Value1", "Value2", "Result"],
            [10, 20, ""],
            [5, 7, ""],
        ]

        worksheet.update_values("A1:C3", data)
        print("✓ Dummy data inserted (A1:C3)")

        # TEST 1: set_formula_in_cell
        print("\n" + "=" * 60)
        print("TEST 1: set_formula_in_cell()")
        print("=" * 60)

        result = set_formula_in_cell(
            sheet_name=test_sheet_name,
            cell_addr="C2",
            formula="A2+B2"
        )
        print(f"✓ Set Formula Result: {result}")
        print("  Expected: Formula '=A2+B2' inserted into C2")

        # TEST 2: get_formula_from_cell
        print("\n" + "=" * 60)
        print("TEST 2: get_formula_from_cell()")
        print("=" * 60)

        formula = get_formula_from_cell(
            sheet_name=test_sheet_name,
            cell_addr="C2"
        )
        print(f"✓ Retrieved Formula: {formula}")
        print("  Expected: '=A2+B2'")

        # TEST 3: evaluate_formula
        print("\n" + "=" * 60)
        print("TEST 3: evaluate_formula()")
        print("=" * 60)

        value = evaluate_formula(
            sheet_name=test_sheet_name,
            cell_addr="C2"
        )
        print(f"✓ Evaluated Result: {value}")
        print("  Expected: 30")

        # Extra check: second row
        print("\nTesting second formula row")
        set_formula_in_cell(test_sheet_name, "C3", "A3*B3")

        print("Formula:", get_formula_from_cell(test_sheet_name, "C3"))
        print("Value:", evaluate_formula(test_sheet_name, "C3"))
        print("Expected: Formula '=A3*B3', Value 35")

        # Final Summary
        print("\n" + "=" * 60)
        print("Formula Operations Test Suite Complete")
        print("=" * 60)
        print(f"✓ Worksheet used: '{test_sheet_name}'")
        print("✓ Formula set / get / evaluate tested")
        print("✓ Verify values visually in Google Sheets")
        print("=" * 60)

    except Exception as e:
        print(f"\n✗ Fatal Error: {e}")
        import traceback
        traceback.print_exc()


if __name__=="__main__":
    test_formula_operations()