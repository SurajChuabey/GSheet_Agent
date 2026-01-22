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

from tools.data_operations.operations import append_data_batch_in_rows

if __name__=="__main__":
    # establish connection with google
    Services.connect()
    # Mocking the CSV input from a user
    test_values = """"John Doe","john@example.com",12345
    "Jane Smith","jane@example.com",67890"""

    # Running the function
    result = append_data_batch_in_rows(sheet_name="Sheet1", row_index=1, values=test_values)

    print(result)
    # transport = os.environ.get(Constants.TRANSPORT,ConfigManager.config(Constants.MCP_SERVER,Constants.TRANSPORT))
    # mcp.run(transport=transport)