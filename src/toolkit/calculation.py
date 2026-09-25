from .errors import DivisionByZeroError


def calculation(tokens: list[str]) -> float:
    expression = list()
    skip_next = False
    for i in range(len(tokens)):
        if skip_next:
            skip_next = False
            continue
        token = tokens[i]
        if token == "u-":
            if i + 1 < len(tokens):
                next_token = tokens[i + 1]
            else:
                next_token = ""
            if next_token != "" and (next_token[0].isdigit() or next_token[0] == "."):
                expression.append(str(-float(next_token)))
                skip_next = True
            else:
                expression.append("0")
                expression.append("-")
        else:
            expression.append(token)
    for _ in range(len(expression)):
        if len(expression) == 1:
            break
        done = False
        for i in range(1, len(expression) - 1):
            if expression[i] in ("*", "/"):
                a = float(expression[i - 1])
                b = float(expression[i + 1])
                if expression[i] == "*":
                    r = a * b
                elif expression[i] == "/":
                    if b == 0:
                        raise DivisionByZeroError("division by zero")
                    r = a / b
                expression[i - 1] = str(r)
                del expression[i:i + 2]
                done = True
                break
        if done:
            continue
        for i in range(1, len(expression) - 1):
            if expression[i] in ("+", "-"):
                a = float(expression[i - 1])
                b = float(expression[i + 1])
                if expression[i] == "+":
                    r = a + b
                elif expression[i] == "-":
                    r = a - b
                expression[i - 1] = str(r)
                del expression[i:i + 2]
                break
    if len(expression) == 0:
        return 0.0
    return float(expression[0])
