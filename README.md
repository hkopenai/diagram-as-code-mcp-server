# Diagram as Code MCP Server

[![GitHub Repository](https://img.shields.io/badge/GitHub-Repository-blue.svg)](https://github.com/hkopenai/hk-prompt-mcp-server)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This is a MCP server to provide mermaid js validation tools and prompt for MCP client

## Why Use This MCP Server?

This MCP server is essential for MCP clients working with Mermaid.js diagrams. Large Language Models (LLMs) might be trained with older data and outdated Mermaid.js syntax, and they may not have enough content trained to effectively fix syntax errors. This server addresses these critical limitations by providing specialized tools to assist in authoring, validating, and automatically fixing Mermaid.js syntax, ensuring diagrams are correctly formatted and functional.

## Features

- No Brackets Description: A prompt to instruct bots to avoid using brackets in descriptions.
- Mermaid.js Support: A tool to assist in authoring, validating, and fixing syntax for Mermaid.js diagrams.

## Setup

1. Clone this repository
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the server:
   ```bash
python -m hkopenai.diagram_as_code_mcp_server
   ```

### Running Options

- Default stdio mode: `python -m hkopenai.diagram_as_code_mcp_server`
- SSE mode (port 8000): `python -m hkopenai.diagram_as_code_mcp_server --sse`
- Serve prompt as tool: `python -m hkopenai.diagram_as_code_mcp_server --tool`

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
      "hkopenai.diagram_as_code_mcp_server",
      "--tool"
    ]
  }
}
```

## Testing

Tests are available in `tests`. Run with:
```bash
pytest
```
