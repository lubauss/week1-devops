# 'test_calculator.py' file
import pytest
from src.calculator import add, div, mul, sub

# addition test
def test_add():
    assert add(1, 1) == 2

# Additional test cases for add function
def test_add_positive():
    assert add(10, 5) == 15

def test_add_negative():
    assert add(-1, -1) == -2

def test_add_zero():
    assert add(0, 0) == 0

def test_add_positive_negative():
    assert add(10, -5) == 5

# subtraction test
def test_sub():
    assert sub(1, 1) == 0

# Additional test cases for sub function
def test_sub_positive():
    assert sub(10, 5) == 5

def test_sub_negative():
    assert sub(-1, -1) == 0

def test_sub_zero():
    assert sub(0, 0) == 0

def test_sub_positive_negative():
    assert sub(10, -5) == 15

# multiplication test
def test_mul():
    assert mul(1, 1) == 1

# Additional test cases for mul function
def test_mul_positive():
    assert mul(10, 5) == 50

def test_mul_negative():
    assert mul(-1, -1) == 1

def test_mul_zero():
    assert mul(0, 5) == 0

def test_mul_positive_negative():
    assert mul(10, -5) == -50

# division test
def test_div():
    assert div(2, 1) == 2

# Additional test cases for div function
def test_div_positive():
    assert div(10, 5) == 2

def test_div_negative():
    assert div(-10, -5) == 2

def test_div_zero_numerator():
    assert div(0, 5) == 0

def test_div_positive_negative():
    assert div(10, -5) == -2

# Test division by zero
def test_div_by_zero():
    with pytest.raises(ZeroDivisionError):
        div(10, 0)

# Additional tests for calculator.py

# Edge cases for division
def test_divide_by_one():
    assert div(5, 1) == 5

def test_divide_by_itself():
    assert div(5, 5) == 1

def test_divide_by_negative():
    assert div(5, -1) == -5

def test_divide_negative_by_negative():
    assert div(-5, -5) == 1

# Edge cases for multiplication
def test_multiply_by_zero():
    assert mul(5, 0) == 0

def test_multiply_by_one():
    assert mul(5, 1) == 5

def test_negative_multiplication():
    assert mul(5, -3) == -15

def test_negative_by_negative_multiplication():
    assert mul(-5, -3) == 15

# Edge cases for subtraction
def test_subtract_zero():
    assert sub(5, 0) == 5

def test_subtract_from_zero():
    assert sub(0, 5) == -5

def test_subtract_negative():
    assert sub(5, -3) == 8

def test_subtract_negative_result():
    assert sub(5, 10) == -5

# Edge cases for addition
def test_add_zero():
    assert add(5, 0) == 5

def test_add_negative():
    assert add(5, -3) == 2

def test_add_negative_result():
    assert add(-5, -3) == -8