from modules import functions
import time

now = time.strftime('%b %d, %Y %H:%M:%S')
print(now)

todos = []

functions.load_todos(todos)

while True:
    command = input("Choose command: ").strip()

    if command.lower().startswith('add'):
        todos.append(command.replace('add', '').strip())
        print(f'{todos[-1]} is now added to the list.')
        functions.save_todos(todos)
    elif 'show' in command.lower():
        functions.show_list(todos)
    elif 'exit' in command.lower():
        break
    elif 'edit' in command.lower() or 'update' in command.lower():
        if functions.handle_empty_list(todos):
            continue
        functions.show_list(todos)
        position = functions.get_position_input(todos, 'edit')
        old_todo_item = todos[position]
        todos[position] = input('Change to: ')
        print(f'{old_todo_item} is now edited to {todos[position]}')
        functions.show_list(todos)
        functions.save_todos(todos)
    elif 'remove' in command.lower():
        if functions.handle_empty_list(todos):
            continue
        functions.show_list(todos)
        position = functions.get_position_input(todos, 'remove')
        print(f'{todos[position]} is removed')
        todos.pop(position)
        functions.show_list(todos)
        functions.save_todos(todos)
    elif 'clear' in command.lower():
        todos.clear()
        functions.save_todos(todos)
    else:
        print('Command is not valid')

print('Bye')
