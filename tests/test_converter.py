import pytest
from src.toolkit.converter import convertation
from src.toolkit.errors import (
    AbsoluteZeroError,
    IncompatibleUnitsError,
    UnknownUnitError,
)


def test_mm_to_cm():
    assert float(convertation('10', 'mm', 'cm')) == 1.0


def test_mm_to_m():
    assert float(convertation('1000', 'mm', 'm')) == 1.0


def test_mm_to_km():
    assert float(convertation('1000000', 'mm', 'km')) == 1.0


def test_cm_to_mm():
    assert float(convertation('1', 'cm', 'mm')) == 10.0


def test_cm_to_m():
    assert float(convertation('100', 'cm', 'm')) == 1.0


def test_cm_to_km():
    assert float(convertation('100000', 'cm', 'km')) == 1.0


def test_m_to_mm():
    assert float(convertation('1', 'm', 'mm')) == 1000.0


def test_m_to_cm():
    assert float(convertation('1', 'm', 'cm')) == 100.0


def test_m_to_km():
    assert float(convertation('1000', 'm', 'km')) == 1.0


def test_km_to_mm():
    assert float(convertation('1', 'km', 'mm')) == 1000000.0


def test_km_to_cm():
    assert float(convertation('1', 'km', 'cm')) == 100000.0


def test_km_to_m():
    assert float(convertation('1', 'km', 'm')) == 1000.0


def test_g_to_kg():
    assert float(convertation('1000', 'g', 'kg')) == 1.0


def test_kg_to_g():
    assert float(convertation('1', 'kg', 'g')) == 1000.0


def test_c_to_k():
    assert float(convertation('0', 'c', 'k')) == 273.0


def test_c_to_f():
    assert float(convertation('0', 'c', 'f')) == 32.0


def test_k_to_c():
    assert float(convertation('273', 'k', 'c')) == 0.0


def test_k_to_f():
    assert float(convertation('273', 'k', 'f')) == 32.0


def test_f_to_c():
    assert float(convertation('32', 'f', 'c')) == 0.0


def test_f_to_k():
    assert float(convertation('32', 'f', 'k')) == 273.0


def test_uppercase_units():
    assert float(convertation('1', 'M', 'CM')) == 100.0


def test_mixed_case_units():
    assert float(convertation('1', 'Km', 'm')) == 1000.0


def test_uppercase_temperature():
    assert float(convertation('0', 'C', 'F')) == 32.0


def test_unknown_from_unit_returns_unchanged():
    with pytest.raises(UnknownUnitError):
        convertation('5', 'xyz', 'm')


def test_unknown_to_unit_returns_unchanged():
    with pytest.raises(UnknownUnitError):
        convertation('5', 'm', 'xyz')


def test_incompatible_units_return_unchanged():
    with pytest.raises(IncompatibleUnitsError):
        convertation('5', 'm', 'kg')


def test_below_absolute_zero_celsius():
    with pytest.raises(AbsoluteZeroError):
        convertation('-300', 'c', 'k')
