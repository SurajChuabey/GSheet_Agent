from mcp.server.fastmcp import FastMCP
from utils.configReader import ConfigManager
from constants.constants import Constants
import os

mcp = FastMCP(
    name=ConfigManager.config(Constants.MCP_SERVER,Constants.NAME),
    instructions=ConfigManager.config(Constants.MCP_SERVER,Constants.DESCRIPTION),
    host=os.environ.get(Constants.MCP_HOST_DEFAULT,ConfigManager.config(Constants.MCP_SERVER, Constants.MCP_HOST_DEFAULT)),
    port=int(os.environ.get(Constants.MCP_PORT_DEFAULT,ConfigManager.config(Constants.MCP_SERVER, Constants.MCP_PORT_DEFAULT))),
)
