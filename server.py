import requests
from mcp.server.fastmcp import FastMCP
import os
import logging

name = "demo-mcp-server"
logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)

logger = logging.getLogger(name)

port = int(os.environ.get('PORT', 12345))
mcp = FastMCP(name, logger=logger, port=port)

@mcp.tool()
def search_keyword(file_path: str, keyword: str):

if __name__ == "__main__":
    logger.info(f"Starting MCP Server on port {port}...")
    try:
        mcp.run(transport="sse")
    except Exception as e:
        logger.error(f"Server error: {str(e)}")
        sys.exit(1)
    finally:
        logger.info("Server terminated")
