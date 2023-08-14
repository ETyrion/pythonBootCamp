import PySimpleGUI as sg

label = sg.Text("Let's Play KBC!!!!")
addBtn = sg.Button("Add")
editBtn = sg.Button("Edit Me")
submitBtn = sg.Button("Submit Btn")
window = sg.Window(title="Hello Audience", layout=[[label], [addBtn, editBtn], [submitBtn]])
window.read()