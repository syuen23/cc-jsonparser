import click
from .lexer import Lexer
from .syntacter import Parser


@click.command()
@click.argument("filename", type=click.Path(exists=True))
def compile_json_file(filename: click.Path) -> bool:
    """Compile a json file for validity

    Args:
        filename (click.Path): Path to json file to parse

    Returns:
        bool: True for valid JSON and False for invalid JSON

    Raises:

    """
    file_contents = read_file(filename)

    tokens = Lexer().tokenize(file_contents)
    result = Parser().parse(tokens)

    return result


def read_file(filename: click.Path) -> str | None:
    """Get string contents of file from path

    Args:
        filename (click.Path): Path to file to read

    Returns:
        str: If file exists, returns contents as string
        None: If file does not exist

    Raises:
        FileNotFoundError: If file does not exist.
    """

    json = None
    try:
        with open(filename, "r") as f:
            json = f.read()
    except FileNotFoundError:
        click.echo("File does not exist")

    return json
