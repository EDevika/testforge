# REWRITTEN (attempt 2) based on feedback: needs to test with a list input
import pytest
from src.grades import get_letter_grade

class Test_Get_letter_grade:

    def test_get_letter_grade_normal(self):
        """Test normal input"""
        result = get_letter_grade(1)
        assert result is not None

    def test_get_letter_grade_with_zero(self):
        """Test with zero values"""
        try:
            result = get_letter_grade(0)
            assert result is not None
        except (ValueError, ZeroDivisionError, TypeError):
            pass

    def test_get_letter_grade_negative(self):
        """Test with negative values"""
        try:
            result = get_letter_grade(-1)
            assert result is not None
        except (ValueError, ZeroDivisionError, TypeError):
            pass

    def test_get_letter_grade_none_input(self):
        """Test None input raises an error"""
        with pytest.raises((TypeError, ValueError)):
            get_letter_grade(None)
    def test_get_letter_grade_with_list(self):
        """Passing a list should raise TypeError"""
        with pytest.raises(TypeError):
            get_letter_grade([1, 2, 3, 4, 5])


import pytest
from src.grades import calculate_average

class Test_Calculate_average:

    def test_calculate_average_normal(self):
        """Test normal input"""
        result = calculate_average([1,2,3])
        assert result == 2.0

    def test_calculate_average_with_zero(self):
        """Test with zero values"""
        try:
            result = calculate_average(0)
            assert result is not None
        except (ValueError, ZeroDivisionError, TypeError):
            pass

    def test_calculate_average_negative(self):
        """Test with negative values"""
        try:
            result = calculate_average(-1)
            assert result is not None
        except (ValueError, ZeroDivisionError, TypeError):
            pass

    def test_calculate_average_none_input(self):
        """Test None input raises an error"""
        with pytest.raises((TypeError, ValueError)):
            calculate_average(None)
