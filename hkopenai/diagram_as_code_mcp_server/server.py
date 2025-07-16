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

def main(host: str = "0.0.0.0", port: int = 5000, sse: bool = False):
    """
    Main function to run the MCP Server.

    Args:
        host: The host address to bind the server to.
        port: The port to listen on.
        sse: Whether to run the server in SSE (Server-Sent Events) mode.
    """
    server = create_mcp_server()

    if sse:
        server.run(transport="streamable-http", host=host, port=port)
        print(f"MCP Server started in SSE mode on port {port}, bound to {host}")
    else:
        server.run()
        print("MCP Server running in stdio mode")

if __name__ == "__main__":
    main()
