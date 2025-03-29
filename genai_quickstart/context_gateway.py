import os

def load_context(file_path: str = "genai_quickstart/context_data.txt") -> str:
    """Loads context from a file and returns it as a string."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()
