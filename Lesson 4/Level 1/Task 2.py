from sys import argv


def read_file_text(path_to_file: str) -> str:
    with open(path_to_file, 'r', encoding='utf-8') as f:
        return f.read()


if __name__ == "__main__":
    # If the file path is absolute
    file_name = argv[0].split("\\")[::-1][0]
    print(f"Text in file is:\n{read_file_text(file_name)}")
    