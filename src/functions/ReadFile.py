import json

def ReadFile(path:str):
    with open(path, "r") as file:
        content = json.loads(file.read())

    return content