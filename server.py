from mcp.server.fastmcp import FastMCP
import os
import sys
import logging

name = "demo-mcp-server"
logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)

logger = logging.getLogger(name)

port = int(os.environ.get('PORT', 12345))
mcp = FastMCP(name, port=port)

@mcp.tool()
def search_keyword(file_path: str, keyword: str):
    try:
        matches = []
        with open(file_path, "r") as file:
            lines = file.readlines()
            for i,line in enumerate(lines):
                words = "".join((char if char.isalnum() else " ") for char in line).split()
                for j,word in enumerate(words):
                    if word == keyword:
                        matches.append({"line_no": i+1, "word": j+1, "line": line[:-1]})
        return {"count": len(matches), "matches": matches}
    except FileNotFoundError:
        return {"error": "File not found"}
    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    logger.info(f"Starting MCP Server on port {port}...")
    try:
        mcp.run(transport="stdio")
    except Exception as e:
        logger.error(f"Server error: {str(e)}")
        sys.exit(1)
    finally:
        logger.info("Server terminated")
