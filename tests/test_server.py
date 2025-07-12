import unittest
from unittest.mock import patch, Mock
from hkopenai.diagram_as_code_mcp_server.server import create_mcp_server


class TestApp(unittest.TestCase):
    @patch("hkopenai.diagram_as_code_mcp_server.server.FastMCP")
    @patch("hkopenai.diagram_as_code_mcp_server.prompt_get_mermaid_js.register")
    @patch("hkopenai.diagram_as_code_mcp_server.tool_fix_mermaid_js.register")
    def test_create_mcp_server(self, mock_tool_register, mock_prompt_register, mock_fastmcp):
        # Setup mocks
        mock_server = Mock()
        mock_fastmcp.return_value = mock_server

        # Test server creation
        server = create_mcp_server()

        # Verify server creation
        mock_fastmcp.assert_called_once()
        self.assertEqual(server, mock_server)

        # Verify that the register functions were called
        mock_prompt_register.assert_called_once_with(mock_server)
        mock_tool_register.assert_called_once_with(mock_server)


if __name__ == "__main__":
    unittest.main()
