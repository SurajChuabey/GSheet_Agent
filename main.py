import os
from services.googleSheetServices import Services
from server import mcp
from utils.configReader import ConfigManager
from constants.constants import Constants
import tools.data_operations.operations
import tools.sheet_operations.operations
import tools.formattings.formattings
import tools.rows_and_coloumns_operations
import tools.formulas.formulas_operations
import tools.sheet_metadata.sheet_metadata_operations
import tools.data_analysis.analysis_operations
import tools.visualizations.visualizations
import services.googleSheetServices

# from tools.sheet_operations.operations import read_sheet

if __name__=="__main__":
    # establish connection with google
    Services.connect()
    # print(read_sheet(sheet_name="Sheet1"))
    transport = os.environ.get(Constants.TRANSPORT,ConfigManager.config(Constants.MCP_SERVER,Constants.TRANSPORT))
    mcp.run(transport=transport)