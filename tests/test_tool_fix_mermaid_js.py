import unittest
from hkopenai.diagram_as_code_mcp_server.tool_fix_mermaid_js import fix_mermaid_js

class TestFixMermaidJs(unittest.TestCase):
    def test_fix_mermaid_js_with_brackets(self):
        input_code = "SaaS -->|10 - Apply Retention Policy (7 days)| SaaS"
        expected_output = "Fix: SaaS -->|\"10 - Apply Retention Policy (7 days)\"| SaaS"
        result = fix_mermaid_js(input_code)
        self.assertEqual(result, expected_output)

    def test_fix_mermaid_js_with_square_brackets(self):
        input_code = "SaaS -->|Policy [Version 1.0]| SaaS"
        expected_output = "Fix: SaaS -->|\"Policy [Version 1.0]\"| SaaS"
        result = fix_mermaid_js(input_code)
        self.assertEqual(result, expected_output)

    def test_fix_mermaid_js_no_brackets(self):
        input_code = "SaaS -->|Simple Description| SaaS"
        expected_output = "No error detected"
        result = fix_mermaid_js(input_code)
        self.assertEqual(result, expected_output)

    def test_fix_mermaid_js_none_input(self):
        from hkopenai.diagram_as_code_mcp_server.prompt_get_mermaid_js import get_mermaid_js
        result = fix_mermaid_js(None)
        self.assertEqual(result, f"No code to review and fix. {get_mermaid_js()}")

    def test_fix_mermaid_js_empty_input(self):
        from hkopenai.diagram_as_code_mcp_server.prompt_get_mermaid_js import get_mermaid_js
        result = fix_mermaid_js("")
        self.assertEqual(result, f"No code to review and fix. {get_mermaid_js()}")

    def test_fix_mermaid_js_whitespace_input(self):
        from hkopenai.diagram_as_code_mcp_server.prompt_get_mermaid_js import get_mermaid_js
        result = fix_mermaid_js("   \n\t  ")
        self.assertEqual(result, f"No code to review and fix. {get_mermaid_js()}")

    def test_fix_mermaid_js_multiple_descriptions(self):
        input_code = "A -->|First (test)| B -->|Second [test]| C"
        expected_output = "Fix: A -->|\"First (test)\"| B -->|\"Second [test]\"| C"
        result = fix_mermaid_js(input_code)
        self.assertEqual(result, expected_output)

    def test_fix_mermaid_js_node_labels_quoting(self):
        input_code = "A[AI Agent 1<br/>(e.g., Chatbot)] ---|Collaborate| B[AI Agent 2<br/>(e.g., Flight Booking)]"
        expected_output = "Fix: A[\"AI Agent 1<br/>(e.g., Chatbot)\"] ---|Collaborate| B[\"AI Agent 2<br/>(e.g., Flight Booking)\"]"
        result = fix_mermaid_js(input_code)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
