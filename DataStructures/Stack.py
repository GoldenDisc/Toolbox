
class stack:

    counter = -1

    def __init__(self, arr=[]):

        self.info = arr

        if len(arr) > 0:

            self.counter = len(arr) - 1
            self.topValue = arr[-1]


    def pushToStack(self, value):

        self.info.append(value)
        self.counter += 1

        self.topValue = self.info[self.counter]


    def popStack(self):

        self.info.pop()
        self.counter -= 1

        self.topValue = self.info[self.counter]
