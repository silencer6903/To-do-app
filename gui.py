import FreeSimpleGUI as sg
from Modules import todo_m
import time



sg.theme("Black")
# Describe lebel, and interface
lebel = sg.Text("Type in to-do")
list_box = sg.Listbox(values=todo_m.get_todo(), key="todos",
                      enable_events=True, size=[45, 10])
label_current_time = sg.Text("", key="clock")

# Input
in_box = sg.InputText(tooltip="Enter text...", key='to_do')

# Buttons
but_add = sg.Button('Add', size=5)
but_edit = sg.Button('Edit')
but_complete = sg.Button("Complete")
but_exit = sg.Button("Exit")

layout = [[lebel, label_current_time], [in_box, but_add],
          [[but_edit, but_complete], list_box],
          [but_exit]]

window = sg.Window("My App to-do",
                   layout=layout,
                   font=('Helvetica', 20))


while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d %Y, %H:%M"))
    match event:
        case 'Add':
            todo = todo_m.get_todo()
            new_todo = values["to_do"] + '\n'

            todo.append(new_todo)
            todo_m.do_todo(todo)
            window['todos'].update(values=todo)
        case 'Edit':
            try:
                ch_val = values['todos'][0]
                new_todo = values['to_do'] + '\n'

                todo = todo_m.get_todo()
                index = todo.index(ch_val)
                todo[index] =  new_todo
                todo_m.do_todo(todo)
                window['todos'].update(values=todo)
            except IndexError:
                sg.popup("Select first item for edit", font=("Helvetica", 20))
        case 'Complete':
            try:
                ch_val = values['todos'][0]

                todo = todo_m.get_todo()
                todo.remove(ch_val)
                todo_m.do_todo(todo)
                window['todos'].update(values=todo)
                window['to_do'].update(value='')
            except IndexError:
                sg.popup("Select first item for complete", font=("Helvetica", 20))
        case 'todos':
            window['to_do'].update(value=values['todos'][0])
        case 'Exit':
            break
        case sg.WIN_CLOSED:
            exit()

