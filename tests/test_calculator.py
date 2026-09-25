import pytest
from src.toolkit.calculation import calculation
from src.toolkit.tokenization import tokenization
from src.toolkit.errors import DivisionByZeroError


def test_addition():
    assert calculation(["1", "+", "2"]) == 3.0


def test_subtraction():
    assert calculation(["10", "-", "4"]) == 6.0


def test_subtraction_negative_result():
    assert calculation(["2", "-", "5"]) == -3.0


def test_multiplication():
    assert calculation(["3", "*", "4"]) == 12.0


def test_multiplication_by_zero():
    assert calculation(["5", "*", "0"]) == 0.0


def test_division():
    assert calculation(["8", "/", "2"]) == 4.0


def test_precedence_mult_before_add():
    assert calculation(["2", "+", "2", "*", "2"]) == 6.0


def test_precedence_div_before_sub():
    assert calculation(["10", "-", "6", "/", "2"]) == 7.0


def test_unary_minus_at_start():
    assert calculation(["u-", "5"]) == -5.0


def test_unary_minus_then_add():
    assert calculation(["u-", "5", "+", "2"]) == -3.0


def test_unary_minus_after_mult():
    assert calculation(["2", "*", "u-", "3"]) == -6.0


def test_two_unary_minus():
    assert calculation(["u-", "2", "*", "u-", "3"]) == 6.0


def test_float_numbers():
    assert calculation(["1.5", "+", "2.25"]) == 3.75


def test_float_multiplication():
    assert calculation(["2.5", "*", "4"]) == 10.0


def test_empty_tokens_returns_zero():
    assert calculation([]) == 0.0


def test_only_unary_minus_returns_zero():
    assert calculation(["u-"]) == 0.0


def test_division_by_zero():
    with pytest.raises(DivisionByZeroError):
        calculation(["1", "/", "0"])


def test_division_by_zero_via_variable():
    with pytest.raises(DivisionByZeroError):
        calculation(["5", "/", "0", "+", "1"])


def test_division_by_zero_after_mult():
    with pytest.raises(DivisionByZeroError):
        calculation(["2", "*", "4", "/", "0"])


def test_full_pipeline():
    tokens = tokenization("2 + 2 * 2")
    assert calculation(tokens) == 6.0


def test_full_pipeline_unary():
    tokens = tokenization("-5 + 2")
    assert calculation(tokens) == -3.0


def test_full_pipeline_div_by_zero():
    with pytest.raises(DivisionByZeroError):
        calculation(tokenization("1 / 0"))
