"""
Main entry point for the Diagram as Code MCP Server.

This module handles command-line arguments and initiates the main server functionality.
"""



from hkopenai_common.cli_utils import cli_main
from .server import server

if __name__ == "__main__":
    cli_main(server, "Diagram as Code MCP Server")
