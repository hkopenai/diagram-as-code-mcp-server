import argparse
from fastmcp import FastMCP
import hkopenai.diagram_as_code_mcp_server.prompt_get_mermaid_js
import hkopenai.diagram_as_code_mcp_server.tool_fix_mermaid_js

def create_mcp_server(use_tool=False):
    """Create and configure the Diagram as code MCP server"""
    mcp = FastMCP(name="DocAsCodeServer")

    hkopenai.diagram_as_code_mcp_server.prompt_get_mermaid_js.register(mcp)
    hkopenai.diagram_as_code_mcp_server.tool_fix_mermaid_js.register(mcp)

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
