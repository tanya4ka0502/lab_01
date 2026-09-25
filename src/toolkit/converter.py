from .errors import AbsoluteZeroError, IncompatibleUnitsError, UnknownUnitError
length = ['mm', 'cm', 'm', 'km']
weight = ['g', 'kg']
temperature = ['c', 'f', 'k']


def convertation(value: str, from_unit: str, to_unit: str) -> float:
    if from_unit.lower() not in length and from_unit.lower() not in weight and from_unit.lower() not in temperature:
        raise UnknownUnitError(f"unknown unit: {from_unit}")
    if to_unit.lower() not in length and to_unit.lower() not in weight and to_unit.lower() not in temperature:
        raise UnknownUnitError(f"unknown unit: {to_unit}")
    if from_unit.lower() in length:
        from_unit_group = 'length'
    elif from_unit.lower() in weight:
        from_unit_group = 'weight'
    elif from_unit.lower() in temperature:
        from_unit_group = 'temperature'
    if to_unit.lower() in length:
        to_unit_group = 'length'
    elif to_unit.lower() in weight:
        to_unit_group = 'weight'
    elif to_unit.lower() in temperature:
        to_unit_group = 'temperature'
    if from_unit_group != to_unit_group:
        raise IncompatibleUnitsError(f"cannot convert {from_unit} to {to_unit}")
    # length converter
    if from_unit.lower() == 'mm':
        if to_unit.lower() == 'cm':
            value = str(float(value) / 10)
        elif to_unit.lower() == 'm':
            value = str(float(value) / 1000)
        elif to_unit.lower() == 'km':
            value = str(float(value) / 1000000)
    elif from_unit.lower() == 'cm':
        if to_unit.lower() == 'mm':
            value = str(float(value) * 10)
        elif to_unit.lower() == 'm':
            value = str(float(value) / 100)
        elif to_unit.lower() == 'km':
            value = str(float(value) / 100000)
    elif from_unit.lower() == 'm':
        if to_unit.lower() == 'mm':
            value = str(float(value) * 1000)
        elif to_unit.lower() == 'cm':
            value = str(float(value) * 100)
        elif to_unit.lower() == 'km':
            value = str(float(value) / 1000)
    elif from_unit.lower() == 'km':
        if to_unit.lower() == 'mm':
            value = str(float(value) * 1000000)
        elif to_unit.lower() == 'cm':
            value = str(float(value) * 100000)
        elif to_unit.lower() == 'm':
            value = str(float(value) * 1000)
    #  weight converter
    elif from_unit.lower() == 'g':
        value = str(float(value) / 1000)
    elif from_unit.lower() == 'kg':
        value = str(float(value) * 1000)
    # temperature converter
    elif from_unit.lower() == 'c':
        if float(value) < -273.0:
            raise AbsoluteZeroError("temperature below absolute zero")
        if to_unit.lower() == 'k':
            value = str(float(value) + 273)
        elif to_unit.lower() == 'f':
            value = str(float(value) * 1.8 + 32)
    elif from_unit.lower() == 'k':
        if float(value) < 0.0:
            raise AbsoluteZeroError("temperature below absolute zero")
        if to_unit.lower() == 'c':
            value = str(float(value) - 273)
        elif to_unit.lower() == 'f':
            value = str((float(value) - 273) * 1.8 + 32)
    elif from_unit.lower() == 'f':
        if float(value) < -459.0:
            raise AbsoluteZeroError("temperature below absolute zero")
        if to_unit.lower() == 'k':
            value = str((float(value) - 32) / 1.8 + 273)
        elif to_unit.lower() == 'c':
            value = str((float(value) - 32) / 1.8)
    # result
    return float(value)
