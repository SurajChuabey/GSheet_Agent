import json
from typing import Optional
from pygsheets.chart import Chart ,ChartType
from server import mcp
from pygsheets import Worksheet
from constants.globals import Global
from utils.utils import utility
from constants.constants import Constants


@mcp.tool(name=Constants.CREATE_CHART_NAME, description=Constants.CREATE_CHART_DESC)
def create_chart(sheet_name: str,chart_type: str = "COLUMN",domain_range: str = "A1:A10",data_ranges: str = "B1:B10",chart_title: str = "My Chart",anchor_cell: str = "E1") -> str:
    """Creates a new chart in the specified worksheet using provided data ranges."""
    try:
        sh: Worksheet = utility._get_worksheet(sheet_name=sheet_name)

        d_start, d_end = domain_range.split(":")
        domain = (d_start, d_end)

        ranges = []
        for r in data_ranges.split(","):
            r_start, r_end = r.strip().split(":")
            ranges.append((r_start, r_end))

        try:
            chart_enum = ChartType[chart_type.upper()]
        except KeyError:
            return f"Invalid chart type: {chart_type}"
        
        sh.add_chart(domain=domain,ranges=ranges,title=chart_title,chart_type=chart_enum,anchor_cell=anchor_cell)
        return f"Chart '{chart_title}' created successfully at {anchor_cell}."

    except Exception as e:
        return f"Error creating chart: {str(e)}"



@mcp.tool(name=Constants.UPDATE_CHART_NAME, description=Constants.UPDATE_CHART_DESC)
def update_chart(sheet_name: str, chart_name: str, updates: str) -> str:
    """Updates an existing chart's properties like title, type, or position."""
    try:
        sh: Worksheet = utility._get_worksheet(sheet_name=sheet_name)
        update_dict = json.loads(updates) if updates else {}

        charts = sh.get_charts()
        target_chart: Chart | None = None

        for c in charts:
            if c.title == chart_name:
                target_chart = c
                break

        if not target_chart:
            return f"Chart with name '{chart_name}' not found."

        if Constants.CHART_TITLE in update_dict:
            target_chart.title = update_dict[Constants.CHART_TITLE]

        if Constants.CHART_TYPE in update_dict:
            try:
                target_chart.chart_type = ChartType[
                    update_dict[Constants.CHART_TYPE].upper()
                ]
            except KeyError:
                return f"Invalid chart type: {update_dict[Constants.CHART_TYPE]}"

        if Constants.ANCHOR_CELL in update_dict:
            target_chart.anchor_cell = update_dict[Constants.ANCHOR_CELL]

        return f"Chart '{chart_name}' updated successfully in '{sheet_name}'."

    except Exception as e:
        return f"Error updating chart: {str(e)}"


@mcp.tool(name=Constants.DELETE_CHART_NAME,description=Constants.DELETE_CHART_DESC)
def delete_chart(sheet_name: str, chart_name: str) -> str:
    """Permanently removes a chart from the worksheet by its title."""
    try:
        sh: Worksheet = utility._get_worksheet(sheet_name=sheet_name)
        charts = sh.get_charts()

        if not charts:
            return "No charts found on the sheet."

        for chart in charts:
            if chart.title == chart_name:
                chart.delete()
                return f"Chart '{chart_name}' deleted successfully."

        return f"Chart with name '{chart_name}' not found."

    except Exception as e:
        return f"Error deleting chart: {str(e)}"
