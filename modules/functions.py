# functions.py

FILE_PATH = 'files/todos.txt'


def save_todos(todos, todos_file=FILE_PATH):
    with open(todos_file, "w") as file:
        for todo in todos:
            file.write(todo + "\n")


def load_todos(todos, todos_file=FILE_PATH):
    todos.clear()
    try:
        with open(todos_file, "r") as file:
            for line in file:
                todos.append(line.strip())
    except FileNotFoundError:
        pass


def get_position_input(todos, do):
    """ Check if the input is a number and within range """
    if len(todos) == 1:
        return 0
    while True:
        position_input = input(f'Which position to {do}? 1-{len(todos)}: ').strip()
        if not position_input.isdigit():
            print('Invalid input. Please enter a number.')
            continue
        _position = int(position_input) - 1
        if _position < 0 or _position > len(todos) - 1:
            print('Position not found. Please enter a valid position.')
            continue
        return _position


def handle_empty_list(todos):
    if not todos:
        print("The list is empty.")
        return True
    return False


def show_list(todos):
    for _index, _item in enumerate(todos):
        print(_index + 1, _item.title())
