import PySimpleGUI as sg

label = sg.Text("Let's Play KBC!!!!")
addBtn = sg.Button("Add")
editBtn = sg.Button("Edit Me")
submitBtn = sg.Button("Submit Btn")
deleteBtn = sg.Button("Delete Btn")
name = sg.Input("Name")
window = sg.Window(title="Hello Audience", layout=[[label], [addBtn, editBtn],[name], [submitBtn, deleteBtn]])
window.read()