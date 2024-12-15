import FreeSimpleGUI as sg
from Modules import todo_m


lebel = sg.Text("Type in to-do")
in_box = sg.InputText(tooltip="Enter text...", key='to_do')
but_add = sg.Button("Add")


window = sg.Window("My App to-do",
                   layout=[[lebel, in_box, but_add]],
                   font=('Helvetica', 10))


while True:
    event, values = window.read()
    match event:
        case 'Add':
            todo = todo_m.get_todo()
            new_todo = values["to_do"] + '\n'
            todo.append(new_todo)
            todo_m.do_todo(todo)
        case sg.WIN_CLOSED:
            break

