import typer
from .calculation import calculation
from .tokenization import tokenization
from .validation import validation
from .converter import convertation

app = typer.Typer(
    name="toolkit",
    help="Console toolkit: calculator and unit converter.",
    no_args_is_help=False,
    add_completion=False,
    pretty_exceptions_enable=False,
)


@app.command()
def calc(
    expression: list[str] = typer.Argument(
        ...,
        help="Arithmetic expression, e.g. '2 + 2 * 2'",
    ),
) -> None:
    expr = " ".join(expression)
    tokens = tokenization(expr)
    tokens = validation(tokens, expr)
    result = calculation(tokens)
    typer.echo(str(result))


@app.command(name="convert")
def convert(
    value: str = typer.Argument(..., help="Numeric value"),
    from_unit: str = typer.Option(..., "--from", help="Source unit"),
    to_unit: str = typer.Option(..., "--to", help="Target unit"),
) -> None:
    result = convertation(value, from_unit, to_unit)
    typer.echo(str(float(result)))


if __name__ == "__main__":
    app()
