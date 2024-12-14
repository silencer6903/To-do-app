import FreeSimpleGUI as sg


lebel = sg.Text("Type in to-do")
in_box = sg.InputText("Enter what to-do...")
but_add = sg.Button("Add")


window = sg.Window("My App to-do", layout=[[lebel, in_box, but_add]])
window.read()
window.close()