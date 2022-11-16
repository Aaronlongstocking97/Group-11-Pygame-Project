import json

class Genrator():

    def __init__(self):
        pass


    def open_file(self, file_name):
        with open(file_name+".json", "r") as my_file:
            if not my_file:
                print("file open failed")
            data = my_file.read()

        obj = json.loads(data)

