
class stack:

    def __init__(self, arr=[]):

        self.arr = arr
        self.counter = len(arr) - 1

        if len(arr) > 0:
            self.topValue = arr[-1]
        
        else:
            self.topValue = None


    def addStack(self, value):

        self.counter += 1
        self.arr.append(value)

        self.topValue = self.arr[self.counter]


    def removeStack(self):

        self.counter -= 1
        self.arr.pop()

        self.topValue = self.arr[self.counter]
