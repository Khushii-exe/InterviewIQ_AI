from pathlib import Path

PROMPT_DIR = Path("prompts")


def load_prompt(filename):
    """
    Load a prompt file from the prompts directory.
    """

    path = PROMPT_DIR / filename

    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def load_all_prompts():

    return {
        "system": load_prompt("system_prompt.md"),
        "rubric": load_prompt("evaluation_rubric.md"),
        "schema": load_prompt("output_schema.json"),
        "examples": load_prompt("examples.md"),
    }