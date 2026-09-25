from .errors import (
    ConsecutiveOperatorsError,
    EmptyExpressionError,
    InvalidCharacterError,
    MissingOperandError,
    MissingOperatorError,
)


def validation(tokens: list[str], expression: str) -> list[str]:
    if expression.strip() == "":
        raise EmptyExpressionError("empty expression")
    if not tokens:
        raise EmptyExpressionError("empty expression")
    for char in expression:
        if char.isspace():
            continue
        if not (char.isdigit() or char in ".+-*/"):
            raise InvalidCharacterError(f"invalid character {char!r}")
    unary_operand = ("u-", "u+")
    binary_operand = ("+", "-", "*", "/")
    expect_operand = True
    for token in tokens:
        if token in unary_operand:
            if not expect_operand:
                raise MissingOperatorError(f"unexpected unary operator {token!r}")
            continue
        if token in binary_operand:
            if expect_operand:
                raise ConsecutiveOperatorsError(f"operator {token!r} without left operand")
            expect_operand = True
            continue
        if not expect_operand:
            raise MissingOperatorError("missing operator between operands")
        expect_operand = False
    if expect_operand:
        raise MissingOperandError("missing operand at end of expression")
    return tokens
