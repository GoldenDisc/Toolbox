
class queue:

    def __init__(self, arr=[]):

        self.arr = arr
        self.back = len(arr) - 1

        if len(arr) > 0:
            self.frontValue = self.arr[0]
        
        else:
            self.frontValue = None


    def addQueue(self, value):

        self.arr.append(value)
        self.back += 1


    def removeQueue(self):

        self.arr.pop()
        self.back -= 1
  
        
    def pushQueue(self):

        self.frontValue = self.arr[1]
        self.arr.pop(0)


class deque:

    def __init__(self, arr=[]):

        self.arr = arr
        self.length = len(arr) - 1

        if len(arr) >= 2:

            self.leftValue = self.arr[0]
            self.rightValue = self.arr[-1]

        elif len(arr) == 1:
            self.leftValue = self.arr[0]
            self.rightValue = self.arr[0]
        
        else:
            self.leftValue = None
            self.rightValue = None


    def addLeftDeque(self, value):

        self.arr.insert(0, value)
        self.leftValue = value
        self.length += 1

        if self.rightValue == None:
            self.rightValue = value


    def removeLeftDeque(self):

        self.leftValue = self.arr[1]
        self.arr.pop(0)
        self.length -= 1

    def addRightDeque(self, value):

        self.arr.append(value)
        self.rightValue = value
        self.length += 1

        if self.leftValue == None:
            self.leftValue = value


    def removeRightDeque(self):

        self.rightValue = self.arr[right - 1]
        self.arr.pop()
        self.length -= 1
