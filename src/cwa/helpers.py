import re

import questionary


def camel_to_snake(text: str) -> str:
    return re.sub(r"(?<!^)(?=[A-Z])", "_", text).lower()


def question(choices, name) -> questionary.Question:
    prompt = camel_to_snake(name).replace("_", " ")  # type: ignore
    return questionary.select(
        f"Select the {prompt}: ",
        choices=choices)  # type: ignore


def binary_question(option: str) -> questionary.Question:
    return questionary.confirm(f"Do you want {option}?", default=False)
