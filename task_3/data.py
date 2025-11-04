from pathlib import Path


def get_data(file_path: str) -> list[str]:
    file_path = Path(file_path)
    if not validate(file_path):
        return []

    try:
        with open(file_path, "r", encoding="UTF-8") as file:
            return file.readlines()
    except (PermissionError, OSError) as e:
        print(f"Cannot read file '{file_path}': {e}")
        return []


def validate(file_path: Path) -> bool:
    if not file_path.exists():
        print("file doesn't exist")
        return False

    if not file_path.is_file():
        print("it is not a file")
        return False

    return True
