
class queue:

    start = 0

    def __init__(self, arr=[]):

        self.info = arr
        self.end = len(arr) - 1


    def addToQueue(self, value):

        self.info.append(value)
        self.end += 1


    def pushQueue(self):
        pass
