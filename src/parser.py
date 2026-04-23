import ast
import re

def parse_python_file(filepath):
    """Read a Python file and extract all function definitions"""
    with open(filepath, 'r') as f:
        source_code = f.read()

    tree = ast.parse(source_code)

    functions = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            functions.append({
                "name": node.name,
                "source": source_code,
                "args": [arg.arg for arg in node.args.args],
                "language": "python"
            })

    return functions


def parse_java_file(filepath):
    """Read a Java file and extract all method definitions"""
    with open(filepath, 'r') as f:
        source_code = f.read()

    # Find all Java methods using regex
    # Matches: public/private/protected + return type + method name + (args)
    pattern = r'(public|private|protected)\s+\w+\s+(\w+)\s*\(([^)]*)\)'
    matches = re.finditer(pattern, source_code)

    functions = []
    for match in matches:
        method_name = match.group(2)
        args_raw = match.group(3)

        # Extract argument names only (ignore types)
        args = []
        if args_raw.strip():
            for arg in args_raw.split(","):
                parts = arg.strip().split()
                if len(parts) >= 2:
                    args.append(parts[-1])  # last part is the name

        functions.append({
            "name": method_name,
            "source": source_code,
            "args": args,
            "language": "java"
        })

    return functions


def parse_file(filepath):
    """Auto-detect language and parse the file"""
    if filepath.endswith(".py"):
        return parse_python_file(filepath)
    elif filepath.endswith(".java"):
        return parse_java_file(filepath)
    else:
        raise ValueError(f"Unsupported file type: {filepath}")