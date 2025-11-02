import requests
from mcp.server.fastmcp import FastMCP
import sys
import os
import random
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


