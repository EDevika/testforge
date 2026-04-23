import os

def generate_tests(function_info, filepath=""):
    """Mock test generator — generates pytest or JUnit 5 tests based on language"""

    function_name = function_info['name']
    args = function_info['args']
    language = function_info.get('language', 'python')

    if language == "java":
        return generate_java_tests(function_name, args, filepath)
    else:
        return generate_python_tests(function_name, args, filepath)


def generate_python_tests(function_name, args, filepath):
    """Generate pytest tests for a Python function"""

    if filepath:
        module_file = os.path.basename(filepath).replace(".py", "")
    else:
        module_file = "calculator"

    return f"""import pytest
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


def generate_java_tests(function_name, args, filepath):
    """Generate JUnit 5 tests for a Java method"""

    if filepath:
        class_name = os.path.basename(filepath).replace(".java", "")
    else:
        class_name = "MyClass"

    # Build test argument strings
    normal_args = ", ".join(["1" if i == 0 else "2" for i in range(len(args))])
    zero_args = ", ".join(["0"] * len(args)) if args else ""
    null_args = ", ".join(["null"] * len(args)) if args else ""

    return f"""import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.Assertions;

public class Test{class_name} {{

    private {class_name} obj = new {class_name}();

    @Test
    void test_{function_name}_normal() {{
        // Test normal input
        var result = obj.{function_name}({normal_args});
        Assertions.assertNotNull(result);
    }}

    @Test
    void test_{function_name}_with_zero() {{
        // Test with zero values
        Assertions.assertDoesNotThrow(() -> {{
            obj.{function_name}({zero_args});
        }});
    }}

    @Test
    void test_{function_name}_negative() {{
        // Test with negative values
        Assertions.assertDoesNotThrow(() -> {{
            obj.{function_name}(-1{", -1" * (len(args) - 1) if len(args) > 1 else ""});
        }});
    }}

    @Test
    void test_{function_name}_null_input() {{
        // Test null input throws exception
        Assertions.assertThrows(Exception.class, () -> {{
            obj.{function_name}({null_args});
        }});
    }}
}}
"""
def regenerate_tests(function_info, filepath, rejection_reason, attempt):
    """Rewrite tests based on the rejection reason"""

    function_name = function_info['name']
    args = function_info['args']
    language = function_info.get('language', 'python')

    if language == "java":
        # For Java, add a comment explaining the fix
        base = generate_java_tests(function_name, args, filepath)
        fix_note = f"// FIXED (attempt {attempt}): {rejection_reason}\n"
        return fix_note + base

    else:
        # For Python, adjust tests based on rejection reason
        if filepath:
            module_file = os.path.basename(filepath).replace(".py", "")
        else:
            module_file = "calculator"

        # Customize based on what the human said was wrong
        extra_test = ""

        if "list" in rejection_reason.lower():
            extra_test = f"""
    def test_{function_name}_with_list(self):
        \"\"\"Fixed: test with proper list input\"\"\"
        result = {function_name}([1, 2, 3, 4, 5])
        assert result is not None"""

        elif "string" in rejection_reason.lower():
            extra_test = f"""
    def test_{function_name}_with_string(self):
        \"\"\"Fixed: test with string input\"\"\"
        with pytest.raises((TypeError, ValueError)):
            {function_name}("invalid_string")"""

        elif "empty" in rejection_reason.lower():
            extra_test = f"""
    def test_{function_name}_empty_input(self):
        \"\"\"Fixed: test with empty input\"\"\"
        with pytest.raises((TypeError, ValueError)):
            {function_name}([])"""

        elif "large" in rejection_reason.lower():
            extra_test = f"""
    def test_{function_name}_large_input(self):
        \"\"\"Fixed: test with very large numbers\"\"\"
        result = {function_name}({", ".join(["999999"] * len(args))})
        assert result is not None"""

        else:
            # Generic improvement — add more edge cases
            extra_test = f"""
    def test_{function_name}_edge_case(self):
        \"\"\"Fixed based on feedback: {rejection_reason}\"\"\"
        try:
            result = {function_name}({", ".join(["0"] * len(args))})
            assert result is not None
        except (TypeError, ValueError):
            pass"""

        return f"""# REWRITTEN (attempt {attempt}) based on feedback: {rejection_reason}
import pytest
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
            {function_name}({", ".join(["None"] * len(args))}){extra_test}
"""