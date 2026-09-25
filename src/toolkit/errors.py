class ToolkitError(Exception):
    exit_code = 2


class EmptyExpressionError(ToolkitError):
    pass


class InvalidCharacterError(ToolkitError):
    pass


class MissingOperandError(ToolkitError):
    pass


class MissingOperatorError(ToolkitError):
    pass


class ConsecutiveOperatorsError(ToolkitError):
    pass


class DivisionByZeroError(ToolkitError):
    pass


class UnknownUnitError(ToolkitError):
    pass


class IncompatibleUnitsError(ToolkitError):
    pass


class AbsoluteZeroError(ToolkitError):
    pass
