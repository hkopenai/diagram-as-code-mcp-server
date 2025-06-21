import argparse
from fastmcp import FastMCP
from typing import Dict, Annotated, Optional
from .prompt_get_mermaid_js import get_mermaid_js

def create_mcp_server(use_tool=False):
    """Create and configure the Document as code MCP server"""
    mcp = FastMCP(name="DocAsCodeServer")

    @mcp.prompt(
        description="Get instructions on authoring mermaid.js",            
    )
    def prompt_mermaid_js_prompt():
        return get_mermaid_js()

    if use_tool:
        @mcp.tool(
            description="Get instructions on authoring mermaid.js",            
        )
        def tool_mermaid_js_prompt():
            return get_mermaid_js()

    return mcp

def main():
    parser = argparse.ArgumentParser(description='HKO MCP Server')
    parser.add_argument('-s', '--sse', action='store_true',
                       help='Run in SSE mode instead of stdio')
    parser.add_argument('-t', '--tool', action='store_true',
                       help='Run in tool mode to serve prompt as a tool')
    args = parser.parse_args()

    server = create_mcp_server(use_tool=args.tool)
    
    if args.sse:
        server.run(transport="streamable-http")
        print("HKO MCP Server running in SSE mode on port 8000")
    else:
        server.run()
        print("HKO MCP Server running in stdio mode")

if __name__ == "__main__":
    main()
