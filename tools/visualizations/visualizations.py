import json
from typing import Optional
from pygsheets.chart import Chart
from server import mcp
from pygsheets import Worksheet
from constants.globals import Global
from utils.utils import utility
from constants.constants import Constants


@mcp.tool(name=Constants.CREATE_CHART_NAME, description=Constants.CREATE_CHART_DESC)
def create_chart(sheet_name:str, chart_type:str, data_range:str, chart_config:str)->str:
    """Creates a chart. chart_config is JSON string (e.g. '{"title":"Sales","x":"A","y":"B"}')."""
    try:
        sh:Worksheet = utility._get_worksheet(sheet_name=sheet_name)
        config = json.loads(chart_config) if chart_config else {}
        chart = sh.add_chart(chart_type=chart_type.upper(), ranges=[data_range], **config)
        return f"Chart created with ID {chart.id}"
    except Exception as e:
        return f"Error creating chart: {str(e)}"


@mcp.tool(name=Constants.UPDATE_CHART_NAME, description=Constants.UPDATE_CHART_DESC)
def update_chart(sheet_name:str, chart_id:int, updates:str)->str:
    """Updates a chart using chart_id. updates is JSON string with chart properties."""
    try:
        sh:Worksheet = utility._get_worksheet(sheet_name=sheet_name)
        update_dict = json.loads(updates) if updates else {}
        chart:Chart = sh.get_charts()[chart_id]
        for k, v in update_dict.items(): setattr(chart, k, v)
        chart.update_chart()
        return f"Chart {chart_id} updated successfully"
    except Exception as e:
        return f"Error updating chart: {str(e)}"


@mcp.tool(name=Constants.DELETE_CHART_NAME, description=Constants.DELETE_CHART_DESC)
def delete_chart(sheet_name:str, chart_id:int)->str:
    """Deletes a chart using its index ID."""
    try:
        sh:Worksheet = utility._get_worksheet(sheet_name=sheet_name)
        charts:Chart = sh.get_charts()
        charts.delete(charts[chart_id])
        return f"Chart {chart_id} deleted successfully"
    except Exception as e:
        return f"Error deleting chart: {str(e)}"
