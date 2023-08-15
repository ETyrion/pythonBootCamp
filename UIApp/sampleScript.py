from BackendCode import addToDoItems as addFunc
from BackendCode import getToDos as getFunc

import PySimpleGUI as sg

label = sg.Text("To Do App")
addBtn = sg.Button("Add New To Do")
editBtn = sg.Button("Edit To Do")
submitBtn = sg.Button("Submit")
cancelBtn = sg.Button("Cancel")
name = sg.InputText(tooltip="Name", key='Name')
window = sg.Window(title="Hello Audience", layout=[[label], [addBtn, editBtn],[name], [submitBtn, cancelBtn]])
event, values = window.read()
print(event)
print(values['Name'])

if event == 'Submit':
    toDoList = getFunc.getToDoList()
    print(toDoList)
    addToDoList = values['Name'] + "\n"
    print(addToDoList)
    toDoList.append(addToDoList)
    addFunc.addToDoList(toDoList)