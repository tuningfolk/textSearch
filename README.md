# textSearch
MCP Server that searches for a word within a file


## Setup
```bash
git clone https://github.com/tuningfolk/textSearch.git
cd textSearch
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```
## Run the server

```bash
python server.py
```

## Testing with MCP Inspector

While the server is running, in a new terminal:
```bash
npx @modelcontextprotocol/inspector
```

Connect via stdio transport.

Choose search_keyword tool and provide:
```bash
{
  "file_path": "examples/file1_system.txt",
  "keyword": "system"
}
```

View JSON output in the right panel.
