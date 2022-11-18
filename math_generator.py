import json
import random

class Generator():

    def __init__(self, filename):
        self.data = self.open_file(filename)


    def open_file(self, filename):
        with open(filename+".json", "r") as my_file:
            if not my_file:
                print("file open failed")
            data = my_file.read()

        obj = json.loads(data)
        obj = list(obj.items())

        return obj

    def generate(self):
        choice = random.randint(0, len(self.data) -1)
        que,ans = self.data.pop(choice)
        return que, ans
