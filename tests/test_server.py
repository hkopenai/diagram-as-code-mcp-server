import unittest
from unittest.mock import patch, Mock
from hkopenai.document_as_code_mcp_server.server import create_mcp_server

class TestServer(unittest.TestCase):
    @patch('hkopenai.document_as_code_mcp_server.server.FastMCP')
    def test_create_mcp_server(self, mock_fastmcp):
        # Setup mocks
        mock_server = Mock()
        
        # Track decorator calls and capture decorated functions
        decorator_calls = []
        decorated_funcs = []
        
        def prompt_decorator(description=None):
            # First call: @prompt(description=...)
            decorator_calls.append(((), {'description': description}))
            
            def decorator(f):
                # Second call: decorator(function)
                decorated_funcs.append(f)
                return f
                
            return decorator
            
        mock_server.prompt = prompt_decorator
        mock_server.prompt.call_args = None  # Initialize call_args
        mock_fastmcp.return_value = mock_server

        # Test server creation
        server = create_mcp_server()

        # Verify server creation
        mock_fastmcp.assert_called_once()
        self.assertEqual(server, mock_server)

        # Verify the prompt was decorated
        self.assertEqual(len(decorator_calls), 1)
        self.assertEqual(len(decorated_funcs), 1)
        
if __name__ == "__main__":
    unittest.main()
