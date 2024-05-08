FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """Read a text file and return the list of to-do items."""
    with open(filepath, "r") as file:
        todos = file.readlines()
    return todos


def write_todos(todos, filepath=FILEPATH):
    """Writes a text file with the list that is passed to the function"""
    with open(filepath, "w") as file:
        file.writelines(todos)

