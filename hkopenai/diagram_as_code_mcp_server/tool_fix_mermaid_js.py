import re
from hkopenai.diagram_as_code_mcp_server.prompt_get_mermaid_js import get_mermaid_js

def fix_mermaid_js(code: str | None) -> str:
    """
    Detects brackets in descriptions between pipe symbols and in node labels in Mermaid.js code and suggests quoting them.
    Args:
        code: A string containing Mermaid.js code, or None.
    Returns:
        A string with descriptions and node labels containing brackets wrapped in double quotes to fix syntax errors, 
        prepended with "Fix: " if changes are made, or "No error detected" if no changes are needed, 
        or "No code to review and fix." with instructions if input is empty or None.
    """
    if code is None or (code.strip() if code else "") == "":
        return f"No code to review and fix. {get_mermaid_js()}"
    result = code
    changed = False
    
    # Pattern to match text between pipe symbols (descriptions)
    pipe_pattern = r'\|([^|]*)\|'
    temp_result = ""
    last_end = 0
    for match in re.finditer(pipe_pattern, result):
        start, end = match.span()
        description = match.group(1)
        # Add the part of the string before the match
        temp_result += result[last_end:start + 1]
        if '(' in description or '[' in description:
            # Suggest quoting the description
            suggestion = f'"{description}"'
            temp_result += suggestion
            changed = True
        else:
            temp_result += description
        temp_result += result[end - 1:end]
        last_end = end
    # Add the remaining part of the string after the last match
    temp_result += result[last_end:]
    result = temp_result
    
    # Pattern to match text within square brackets for node labels (e.g., A[...])
    node_pattern = r'(\w+)\[([^\]]*)\]'
    temp_result = ""
    last_end = 0
    for match in re.finditer(node_pattern, result):
        start, end = match.span()
        node_name = match.group(1)
        label = match.group(2)
        # Add the part of the string before the match
        temp_result += result[last_end:start]
        if '<br/>' in label or '(' in label or '[' in label:
            # Suggest quoting the label
            suggestion = f'{node_name}["{label}"]'
            temp_result += suggestion
            changed = True
        else:
            temp_result += result[start:end]
        last_end = end
    # Add the remaining part of the string after the last match
    temp_result += result[last_end:]
    result = temp_result
    
    if changed:
        return "Fix: " + result
    return "No error detected"
