"""Module for testing the Mermaid.js syntax fixing tool."""

import unittest
from unittest.mock import MagicMock, patch

from hkopenai.diagram_as_code_mcp_server.tool_fix_mermaid_js import _fix_mermaid_js, register
from hkopenai.diagram_as_code_mcp_server.prompt_get_mermaid_js import _get_mermaid_js


class TestFixMermaidJs(unittest.TestCase):
    """Test class for verifying Mermaid.js syntax fixing functionality."""

    def test_fix_mermaid_js_with_brackets(self):
        """Test fixing descriptions with parentheses."""
        input_code = "SaaS -->|10 - Apply Retention Policy (7 days)| SaaS"
        expected_output = """Fix: SaaS -->|"10 - Apply Retention Policy (7 days)"| SaaS"""
        result = _fix_mermaid_js(input_code)
        self.assertEqual(result, expected_output)

    def test_fix_mermaid_js_with_square_brackets(self):
        """Test fixing descriptions with square brackets."""
        input_code = "SaaS -->|Policy [Version 1.0]| SaaS"
        expected_output = """Fix: SaaS -->|"Policy [Version 1.0]"| SaaS"""
        result = _fix_mermaid_js(input_code)
        self.assertEqual(result, expected_output)

    def test_fix_mermaid_js_no_brackets(self):
        """Test code with no brackets in descriptions."""
        input_code = "SaaS -->|Simple Description| SaaS"
        expected_output = "No error detected"
        result = _fix_mermaid_js(input_code)
        self.assertEqual(result, expected_output)

    def test_fix_mermaid_js_none_input(self):
        """Test with None as input code."""
        result = _fix_mermaid_js(None)
        self.assertEqual(result, f"No code to review and fix. {_get_mermaid_js()}")

    def test_fix_mermaid_js_empty_input(self):
        """Test with empty string as input code."""
        result = _fix_mermaid_js("")
        self.assertEqual(result, f"No code to review and fix. {_get_mermaid_js()}")

    def test_fix_mermaid_js_whitespace_input(self):
        """Test with whitespace string as input code."""
        result = _fix_mermaid_js("   \n\t  ")
        self.assertEqual(result, f"No code to review and fix. {_get_mermaid_js()}")

    def test_fix_mermaid_js_multiple_descriptions(self):
        """Test with multiple descriptions in one line."""
        input_code = "A -->|First (test)| B -->|Second [test]| C"
        expected_output = """Fix: A -->|"First (test)"| B -->|"Second [test]"| C"""
        result = _fix_mermaid_js(input_code)
        self.assertEqual(result, expected_output)

    def test_fix_mermaid_js_node_labels_quoting(self):
        """Test fixing node labels with special characters."""
        input_code = "A[AI Agent 1<br/>(e.g., Chatbot)] ---|Collaborate| B[AI Agent 2<br/>(e.g., Flight Booking)]"
        expected_output = "Fix: A[\"AI Agent 1<br/>(e.g., Chatbot)\"] ---|Collaborate| B[\"AI Agent 2<br/>(e.g., Flight Booking)\"]"
        result = _fix_mermaid_js(input_code)
        self.assertEqual(result, expected_output)

    def test_register_tool(self):
        """Test the registration of the fix_mermaid_js tool."""
        mock_mcp = MagicMock()
        register(mock_mcp)
        mock_mcp.tool.assert_called_once_with(
            description="A tool to provide instructions on authoring, validating or fixing syntax in mermaid.js"
        )
        decorated_function = mock_mcp.tool.return_value.call_args[0][0]
        self.assertEqual(decorated_function.__name__, "fix_mermaid_js_tool")
        with patch("hkopenai.diagram_as_code_mcp_server.tool_fix_mermaid_js._fix_mermaid_js") as mock_fix_mermaid_js:
            decorated_function(code="test code")
            mock_fix_mermaid_js.assert_called_once_with("test code")


if __name__ == '__main__':
    unittest.main()
