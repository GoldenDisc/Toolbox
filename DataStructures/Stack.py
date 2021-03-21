
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


    def __iter__(self):
        return self

    
    def __next__(self):
        if self.counter == -1:
            raise StopIteration
        
        current = self.topValue
        self.removeStack()

        return current


test_stack = stack(["BLAST OFF!", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

for value in test_stack:
    print(f"Value: {value}, Length: {test_stack.counter}")
