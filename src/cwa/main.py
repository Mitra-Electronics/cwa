from typer import Typer
from . import create

app = Typer()
app.add_typer(create.app, name="create")
