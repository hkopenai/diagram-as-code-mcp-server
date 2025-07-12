"""Module for providing Mermaid.js related prompts."""
from fastmcp import FastMCP

def register(mcp: FastMCP):
    """Registers the get_mermaid_js prompt with the FastMCP server."""
    @mcp.prompt(
        description="A tool to provide instructions on authoring, validating or fixing syntax in mermaid.js",
    )
    def prompt_mermaid_js_prompt():
        return _get_mermaid_js()

def _get_mermaid_js() -> str:
    """
    Get instructions on authoring mermaid.js.
    Returns a string with the prompt instructions.
    """
    return "In descriptions or responses, quote the description or avoid using brackets such as (), [], or {} for syntax error."
