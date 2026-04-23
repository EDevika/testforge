import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.Assertions;

public class TestCalculator {

    private Calculator obj = new Calculator();

    @Test
    void test_add_normal() {
        // Test normal input
        var result = obj.add(1, 2);
        Assertions.assertNotNull(result);
    }

    @Test
    void test_add_with_zero() {
        // Test with zero values
        Assertions.assertDoesNotThrow(() -> {
            obj.add(0, 0);
        });
    }

    @Test
    void test_add_negative() {
        // Test with negative values
        Assertions.assertDoesNotThrow(() -> {
            obj.add(-1, -1);
        });
    }

    @Test
    void test_add_null_input() {
        // Test null input throws exception
        Assertions.assertThrows(Exception.class, () -> {
            obj.add(null, null);
        });
    }
}


import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.Assertions;

public class TestCalculator {

    private Calculator obj = new Calculator();

    @Test
    void test_divide_normal() {
        // Test normal input
        var result = obj.divide(1, 2);
        Assertions.assertNotNull(result);
    }

    @Test
    void test_divide_with_zero() {
        // Test with zero values
        Assertions.assertDoesNotThrow(() -> {
            obj.divide(0, 0);
        });
    }

    @Test
    void test_divide_negative() {
        // Test with negative values
        Assertions.assertDoesNotThrow(() -> {
            obj.divide(-1, -1);
        });
    }

    @Test
    void test_divide_null_input() {
        // Test null input throws exception
        Assertions.assertThrows(Exception.class, () -> {
            obj.divide(null, null);
        });
    }
}


import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.Assertions;

public class TestCalculator {

    private Calculator obj = new Calculator();

    @Test
    void test_multiply_normal() {
        // Test normal input
        var result = obj.multiply(1, 2);
        Assertions.assertNotNull(result);
    }

    @Test
    void test_multiply_with_zero() {
        // Test with zero values
        Assertions.assertDoesNotThrow(() -> {
            obj.multiply(0, 0);
        });
    }

    @Test
    void test_multiply_negative() {
        // Test with negative values
        Assertions.assertDoesNotThrow(() -> {
            obj.multiply(-1, -1);
        });
    }

    @Test
    void test_multiply_null_input() {
        // Test null input throws exception
        Assertions.assertThrows(Exception.class, () -> {
            obj.multiply(null, null);
        });
    }
}
