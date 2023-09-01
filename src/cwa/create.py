from questionary import form
from typer import Typer, echo

from cwa.helpers import binary_question, question
from cwa.generators import gen_venv
from cwa.config import packages

app = Typer()


@app.command("project")
def project():
    result = form(
        package=question(packages, "package manager"),
        pre_commit=binary_question("pre commit"),
        docker=binary_question("docker"),
    ).ask()
    echo(result)
    gen_venv(result["package"])
