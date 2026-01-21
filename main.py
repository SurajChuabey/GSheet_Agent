from services.googleSheetServices import Services
from server import mcp
from utils.configReader import ConfigManager
from constants.constants import Constants
import tools.data_operations.operations
import tools.sheet_operations.operations

if __name__=="__main__":
    # establish connection with google
    Services.connect()
    mcp.run(
        transport=ConfigManager.config(Constants.MCP_SERVER,Constants.TRANSPORT),
    )