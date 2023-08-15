FilePath = "../filesData/toDoList.txt"

def addToDoList(toDoItems):
    with open(FilePath, 'a') as file:
       file.writelines(toDoItems)