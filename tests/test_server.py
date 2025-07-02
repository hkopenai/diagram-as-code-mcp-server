import unittest
from unittest.mock import patch, Mock
from hkopenai.diagram_as_code_mcp_server.server import create_mcp_server

class TestApp(unittest.TestCase):
    @patch('hkopenai.diagram_as_code_mcp_server.server.FastMCP')
    @patch('hkopenai.diagram_as_code_mcp_server.server.get_mermaid_js')
    @patch('hkopenai.diagram_as_code_mcp_server.server.fix_mermaid_js')
    def test_create_mcp_server(self, mock_fix_mermaid_js, mock_get_mermaid_js, mock_fastmcp):
        # Setup mocks
        mock_server = Mock()
        
        # Configure mock_server.prompt and mock_server.tool to return a mock that acts as the decorator
        mock_server.prompt.return_value = Mock()
        mock_server.tool.return_value = Mock()
        mock_fastmcp.return_value = mock_server

        # Test server creation
        server = create_mcp_server()

        # Verify server creation
        mock_fastmcp.assert_called_once()
        self.assertEqual(server, mock_server)

        # Verify that the prompt and tool decorators were called
        self.assertEqual(mock_server.prompt.call_count, 1)
        self.assertEqual(mock_server.tool.call_count, 1)

        # Get all decorated functions
        decorated_prompts = {call.args[0].__name__: call.args[0] for call in mock_server.prompt.return_value.call_args_list}
        decorated_tools = {call.args[0].__name__: call.args[0] for call in mock_server.tool.return_value.call_args_list}
        
        self.assertEqual(len(decorated_prompts), 1)
        self.assertEqual(len(decorated_tools), 1)

        # Call each decorated function and verify that the correct underlying function is called
        
        decorated_prompts['prompt_mermaid_js_prompt']()
        mock_get_mermaid_js.assert_called_once_with()

        decorated_tools['tool_mermaid_js_prompt'](code="test code")
        mock_fix_mermaid_js.assert_called_once_with("test code")

if __name__ == "__main__":
    unittest.main()
