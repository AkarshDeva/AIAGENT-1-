from langchain_core.tools import tool


@tool
def multiply(a: float, b: float) -> float:
    """Multiplies two numbers."""
    return a * b


@tool
def save_note(text: str) -> str:
    """Saves a note to a file."""
    with open("notes.txt", "a", encoding="utf-8") as f:
        f.write(text + "\n")

    return "Note saved."


All_Tools = [multiply, save_note]