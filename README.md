# HK Prompt MCP Server

[![GitHub Repository](https://img.shields.io/badge/GitHub-Repository-blue.svg)](https://github.com/hkopenai/hk-prompt-mcp-server)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This is an MCP server that provides custom prompts for guiding bot interactions.

## Features

- No Brackets Description: A prompt to instruct bots to avoid using brackets in descriptions.

## Setup

1. Clone this repository
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the server:
   ```bash
   python -m hkopenai.document_as_code_mcp_server
   ```

### Running Options

- Default stdio mode: `python -m hkopenai.document_as_code_mcp_server`
- SSE mode (port 8000): `python -m hkopenai.document_as_code_mcp_server --sse`
- Serve prompt as tool: `python -m hkopenai.document_as_code_mcp_server --tool`

## Cline Integration

Cline does not support prompt from mcp server at this moment. The prompt is provided as tool:

To connect this MCP server to Cline using stdio:

1. Add this configuration to your Cline MCP settings (cline_mcp_settings.json):
```json
{
  "hk-prompt-server": {
    "disabled": false,
    "timeout": 3,
    "type": "stdio",
    "command": "python",
    "args": [
      "-m",
      "hkopenai.document_as_code_mcp_server",
      "--tool"
    ]
  }
}
```

## Testing

Tests are available in `tests`. Run with:
```bash
pytest
