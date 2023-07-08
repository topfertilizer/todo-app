from modules import functions as f
import PySimpleGUI as sg
import time

sg.theme('DarkPurple4')

todos = []

f.load_todos(todos)

now = time.strftime('%b %d, %Y %H:%M:%S')

clock = sg.Text(now, key='clock')
label = sg.Text('Type in a To-Do')
output = sg.Text(key='output', text_color='green', background_color='black')

input_box = sg.InputText(tooltip='Enter todo', key='todo', size=41)
list_box = sg.Listbox(values=todos, key='todos',
                      enable_events=True, size=(40, 10))

add_button = sg.Button('Add')
edit_button = sg.Button('Edit')
remove_button = sg.Button('Remove')
clear_button = sg.Button('Clear')

layout = [[clock],
          [label],
          [input_box, add_button],
          [list_box, edit_button],
          [remove_button, clear_button, output]]

window = sg.Window('My To-Do App',
                   layout=layout,
                   font=('Helvetica', 15))

while True:
    event, values = window.read(timeout=1000)
    window['clock'].update(value=time.strftime('%b %d, %Y %H:%M:%S'))

    print(event)
    print(values)

    match event:
        case 'Add':
            todos.append(values['todo'])

            note = f'{todos[-1]} is now added to the list.'
            print(note)

            f.save_todos(todos)
            window['output'].update(value=note)
            window['todo'].update(value='')
            window['todos'].update(values=todos)
        case sg.WINDOW_CLOSED:
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case 'Edit':
            if f.handle_empty_list(todos):
                continue

            try:
                position = todos.index(values['todos'][0])

                old_todo_item = todos[position]
                new_todo_item = values['todo']
                todos[position] = new_todo_item

                note = f'{old_todo_item} is now edited to {todos[position]}'
                print(note)

                f.save_todos(todos)
                window['output'].update(value=note)
                window['todo'].update(value='')
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup('Please select an item first',
                         font=('Helvetica', 17))
        case 'Remove':
            if f.handle_empty_list(todos):
                continue

            try:
                position = todos.index(values['todos'][0])

                todo_item = todos[position]
                todos.pop(position)

                note = f'{todo_item} is removed'
                print(note)

                f.save_todos(todos)
                window['output'].update(value=note)
                window['todo'].update(value='')
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup('Please select an item first',
                         font=('Helvetica', 17))
        case 'Clear':
            todos.clear()
            f.save_todos(todos)
            window['todos'].update(values=todos)

window.close()
