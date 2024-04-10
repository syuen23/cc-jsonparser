import click


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
