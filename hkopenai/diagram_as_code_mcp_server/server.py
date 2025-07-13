"""Module for creating and running the Diagram as Code MCP Server."""
from fastmcp import FastMCP
import hkopenai.diagram_as_code_mcp_server.prompt_get_mermaid_js
import hkopenai.diagram_as_code_mcp_server.tool_fix_mermaid_js

def create_mcp_server():
    """Create and configure the Diagram as code MCP server"""
    mcp = FastMCP(name="DocAsCodeServer")

    hkopenai.diagram_as_code_mcp_server.prompt_get_mermaid_js.register(mcp)
    hkopenai.diagram_as_code_mcp_server.tool_fix_mermaid_js.register(mcp)

    return mcp

def main(host: str, port: int, sse: bool):
    """
    Main function to run the MCP Server.

    Args:
        args: Command line arguments passed to the function.
    """
    server = create_mcp_server()

    if sse:
        server.run(transport="streamable-http", host=host, port=port)
        print(f"MCP Server started in SSE mode on port {args.port}, bound to {args.host}")
    else:
        server.run()
        print("MCP Server running in stdio mode")

if __name__ == "__main__":
    main()
