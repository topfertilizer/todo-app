from modules import functions as f
import PySimpleGUI as sg

todos = []

f.load_todos(todos)

label = sg.Text('Type in a To-Do')
input_box = sg.InputText(tooltip='Enter todo', key='todo')
add_button = sg.Button('Add')

window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
            todos.append(values['todo'])
            print(f'{todos[-1]} is now added to the list.')
            f.save_todos(todos)
        case sg.WINDOW_CLOSED:
            break

window.close()
