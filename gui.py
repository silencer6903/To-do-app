import FreeSimpleGUI as sg
from FreeSimpleGUI import Input, InputText

from Modules import todo_m


# Describe lebel, and interface
lebel = sg.Text("Type in to-do")
list_box = sg.Listbox(values=todo_m.get_todo(), key="todos",
                      enable_events=True, size=[45, 10])

# Input
in_box = sg.InputText(tooltip="Enter text...", key='to_do')

# Buttons
but_add = sg.Button('Add')
but_edit = sg.Button('Edit')

window = sg.Window("My App to-do",
                   layout=[[lebel],
                           [in_box, but_add],
                           [list_box, but_edit]],
                   font=('Helvetica', 20))


while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
            todo = todo_m.get_todo()
            new_todo = values["to_do"] + '\n'

            todo.append(new_todo)
            todo_m.do_todo(todo)
            window['todos'].update(values=todo)
        case 'Edit':
            ch_val = values['todos'][0]
            new_todo = values['to_do'] + '\n'

            todo = todo_m.get_todo()
            index = todo.index(ch_val)
            todo[index] =  new_todo
            todo_m.do_todo(todo)
            window['todos'].update(values=todo)
        case 'todos':
            window['to_do'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

