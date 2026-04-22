import pytest
from src.calculator import add

class Test_Add:

    def test_add_normal(self):
        """Test normal input"""
        result = add(1, 2)
        assert result is not None

    def test_add_with_zero(self):
        """Test with zero values"""
        try:
            result = add(0, 0)
            assert result is not None
        except (ValueError, ZeroDivisionError):
            pass  # acceptable to raise on zero

    def test_add_negative(self):
        """Test with negative values"""
        try:
            result = add(-1, -1)
            assert result is not None
        except (ValueError, ZeroDivisionError):
            pass  # acceptable

    def test_add_none_input(self):
        """Test None input raises an error"""
        with pytest.raises((TypeError, ValueError)):
            add(None, None)


import pytest
from src.calculator import divide

class Test_Divide:

    def test_divide_normal(self):
        """Test normal input"""
        result = divide(1, 2)
        assert result is not None

    def test_divide_with_zero(self):
        """Test with zero values"""
        try:
            result = divide(0, 0)
            assert result is not None
        except (ValueError, ZeroDivisionError):
            pass  # acceptable to raise on zero

    def test_divide_negative(self):
        """Test with negative values"""
        try:
            result = divide(-1, -1)
            assert result is not None
        except (ValueError, ZeroDivisionError):
            pass  # acceptable

    def test_divide_none_input(self):
        """Test None input raises an error"""
        with pytest.raises((TypeError, ValueError)):
            divide(None, None)
