import re


def tokenization(expression: str) -> list[str]:
    pattern = r"\d+\.\d*|\.\d+|\d+|//|[-+*/]"
    new_expression = re.findall(pattern, expression)
    tokens = list()
    expect_operand = True
    for token in new_expression:
        if token in ("+", "-"):
            if expect_operand:
                if token == "-":
                    tokens.append("u-")
            else:
                tokens.append(token)
                expect_operand = True
        elif token in ("*", "/"):
            tokens.append(token)
            expect_operand = True
        else:
            tokens.append(token)
            expect_operand = False
    return tokens
