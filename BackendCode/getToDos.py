FilePath = "../filesData/toDoList.txt"

def getToDoList():
    with open(FilePath, 'r') as file:
        toDoItemsList = file.readlines()

    return toDoItemsList

#getToDoList()