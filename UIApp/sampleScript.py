import PySimpleGUI as sg

label = sg.Text("Let's Play KBC!!!!")
addBtn = sg.Button("Add")
submitBtn = sg.Button("Submit Btn")
window = sg.Window(title="Hello Audience", layout=[[label], [addBtn], [submitBtn]])
window.read()