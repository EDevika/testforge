import ast

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
                "args": [arg.arg for arg in node.args.args]
            })

    return functions