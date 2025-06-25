import re
from hkopenai.document_as_code_mcp_server.prompt_get_mermaid_js import get_mermaid_js

def fix_mermaid_js(code: str | None) -> str:
    """
    Detects brackets in descriptions between pipe symbols in Mermaid.js code and suggests quoting them.
    Args:
        code: A string containing Mermaid.js code, or None.
    Returns:
        A string with descriptions containing brackets wrapped in double quotes to fix syntax errors, 
        prepended with "Fix: " if changes are made, or "No error detected" if no changes are needed, 
        or "No code to review and fix." with instructions if input is empty or None.
    """
    if code is None or (code.strip() if code else "") == "":
        return f"No code to review and fix. {get_mermaid_js()}"
    # Pattern to match text between pipe symbols
    pattern = r'\|([^|]*)\|'
    result = code
    matches = re.finditer(pattern, code)
    offset = 0
    changed = False
    for match in matches:
        description = match.group(1)
        if '(' in description or '[' in description:
            # Suggest quoting the description
            start, end = match.span()
            suggestion = f'"{description}"'
            result = result[:start+offset+1] + suggestion + result[end+offset-1:]
            offset += len(suggestion) - len(description) + 2  # Adjust for added quotes
            changed = True
    if changed:
        return "Fix: " + result
    return "No error detected"
