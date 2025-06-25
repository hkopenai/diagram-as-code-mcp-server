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
    result = ""
    last_end = 0
    changed = False
    for match in re.finditer(pattern, code):
        start, end = match.span()
        description = match.group(1)
        # Add the part of the string before the match
        result += code[last_end:start + 1]
        if '(' in description or '[' in description:
            # Suggest quoting the description
            suggestion = f'"{description}"'
            result += suggestion
            changed = True
        else:
            result += description
        result += code[end - 1:end]
        last_end = end
    # Add the remaining part of the string after the last match
    result += code[last_end:]
    if changed:
        return "Fix: " + result
    return "No error detected"
