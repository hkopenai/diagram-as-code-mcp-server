import argparse
from fastmcp import FastMCP
from typing import Dict, Annotated, Optional
from pydantic import Field
from .prompt_get_mermaid_js import get_mermaid_js
from .tool_fix_mermaid_js import fix_mermaid_js

def create_mcp_server(use_tool=False):
    """Create and configure the Diagram as code MCP server"""
    mcp = FastMCP(name="DocAsCodeServer")

    @mcp.prompt(
        description="A tool to provide instructions on authoring, validating or fixing syntax in mermaid.js",            
    )
    def prompt_mermaid_js_prompt():
        return get_mermaid_js()

    @mcp.tool(
        description="A tool to provide instructions on authoring, validating or fixing syntax in mermaid.js",            
    )
    def tool_mermaid_js_prompt(
        code: Annotated[Optional[str], Field(description="mermaid js code block")]            
    ):
        return fix_mermaid_js(code)

    return mcp

def main(args):
    server = create_mcp_server(use_tool=args.tool)
    
    if args.sse:
        server.run(transport="streamable-http", host=args.host, port=args.port)
        print(f"MCP Server started in SSE mode on port {args.port}, bound to {args.host}")
    else:
        server.run()
        print("MCP Server running in stdio mode")

if __name__ == "__main__":
    main()
