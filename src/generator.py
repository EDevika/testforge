import os

def generate_tests(function_info, filepath=""):
    """Mock test generator — simulates what Claude AI would return"""

    function_name = function_info['name']
    args = function_info['args']

    # Figure out the correct module name from the filepath
    if filepath:
        module_file = os.path.basename(filepath).replace(".py", "")
    else:
        module_file = "calculator"

    mock_test = f"""import pytest
from src.{module_file} import {function_name}

class Test_{function_name.capitalize()}:

    def test_{function_name}_normal(self):
        \"\"\"Test normal input\"\"\"
        result = {function_name}({", ".join(["1" if i == 0 else "2" for i in range(len(args))])})
        assert result is not None

    def test_{function_name}_with_zero(self):
        \"\"\"Test with zero values\"\"\"
        try:
            result = {function_name}({", ".join(["0"] * len(args))})
            assert result is not None
        except (ValueError, ZeroDivisionError, TypeError):
            pass

    def test_{function_name}_negative(self):
        \"\"\"Test with negative values\"\"\"
        try:
            result = {function_name}({", ".join(["-1"] * len(args))})
            assert result is not None
        except (ValueError, ZeroDivisionError, TypeError):
            pass

    def test_{function_name}_none_input(self):
        \"\"\"Test None input raises an error\"\"\"
        with pytest.raises((TypeError, ValueError)):
            {function_name}({", ".join(["None"] * len(args))})
"""

    return mock_test