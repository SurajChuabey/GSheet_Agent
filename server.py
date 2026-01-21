from mcp.server.fastmcp import FastMCP
from utils.configReader import ConfigManager
from constants.constants import Constants

mcp = FastMCP(
    name=ConfigManager.config(Constants.MCP_SERVER,Constants.NAME),
    instructions=ConfigManager.config(Constants.MCP_SERVER,Constants.DESCRIPTION),
    host=ConfigManager.config(Constants.MCP_SERVER, Constants.MCP_HOST_DEFAULT),
    port=int(ConfigManager.config(Constants.MCP_SERVER, Constants.MCP_PORT_DEFAULT)),
)
