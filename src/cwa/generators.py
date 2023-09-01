from subprocess import run, DEVNULL
from typer import echo
import sys
from cwa.config import DEFAULT_VENV_NAME


def gen_venv(manager):
    match manager:
        case "pip":
            run(
                [sys.executable, "-m", "pip", "install", "virtualenv"],
                stdout=DEVNULL,
                check=True
            )
            echo("Installed virtualenv", color=True)
            run(
                [sys.executable, "-m", "virtualenv", DEFAULT_VENV_NAME],
                stdout=DEVNULL,
                check=True
            )
            echo("Created virtualenv")
        case "poetry":
            run(
                [sys.executable, "-m", "pip", "install", "poetry"],
                stdout=DEVNULL,
                check=True
            )
            echo("Installed poetry")
            run(
                ["poetry"]
            )
