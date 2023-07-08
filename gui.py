from modules import functions as f
import PySimpleGUI as sg

todos = []

f.load_todos(todos)

label = sg.Text('Type in a To-Do')
input_box = sg.InputText(tooltip='Enter todo', key='todo', size=41)
add_button = sg.Button('Add')
list_box = sg.Listbox(values=todos, key='todos',
                      enable_events=True, size=(40, 10))
edit_button = sg.Button('Edit')

window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button],
                           [list_box, edit_button]],
                   font=('Helvetica', 15))

while True:
    event, values = window.read()
    print(event)
    print(values)

    match event:
        case 'Add':
            todos.append(values['todo'])
            print(f'{todos[-1]} is now added to the list.')
            f.save_todos(todos)
            window['todos'].update(values=todos)
        case sg.WINDOW_CLOSED:
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case 'Edit':
            if f.handle_empty_list(todos):
                continue
            position = todos.index(values['todos'][0])
            old_todo_item = todos[position]
            new_todo_item = values['todo']
            todos[position] = new_todo_item
            print(f'{old_todo_item} is now edited to {todos[position]}')
            f.save_todos(todos)
            window['todos'].update(values=todos)

window.close()
