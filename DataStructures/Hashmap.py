from LinkedListAndTree import Node


def alph_int(char):
    return ord(char.lower()) - 96


class hash_iter:

    def __init__(self, keys):
        self.index = 0
        self.keys = keys


    def __next__(self):
        
        if self.index == len(self.keys):

            self.index = 0
            raise StopIteration

        else:

            current = self.keys[self.index]
            self.index += 1

            return current

class hashmap:
    
    def __init__(self, arr=None, length=20):

        self.keys = []
        self.arr = [Node(None) for x in range(length)]

        if arr == None:
        
            self.count = 0

        elif len(arr) % 2 == 1:
            raise Exception("The list given as an argument when creating a 'hashmap' object must contain an even number of objects.")

        else:

            self.count = len(arr)//2

            for num in [x for x in range(len(arr)) if x % 2 == 0]:

                key = str(arr[num])
                value = arr[num + 1]
                index = (alph_int(key[0]) * alph_int(key[-1]) * len(key)) % length

                self.keys.append(key)

                if self.arr[index].value == None:
                    self.arr[index] = Node((key, value))

                elif self.arr[index].value[0] == key:
                    self.arr[index] = Node((key, value))

                else:

                    current_node = self.arr[index]

                    while current_node.next != None:

                        if current_node.next.value[0] == key:
                            break

                        current_node = current_node.next

                    current_node.next = Node((key, value))


    def hash_func(self, key):
        return (alph_int(key[0]) * alph_int(key[-1]) * len(key)) % len(self.arr)


    def hash_insert(self, key, value):

        index = self.hash_func(key)

        if self.arr[index].value == None:
            self.arr[index] = Node((key, value))

        elif self.arr[index].value[0] == key:
            self.arr[index] = Node((key, value))

        else:

            current_node = self.arr[index]

            while current_node.next != None:

                if current_node.next.value[0] == key:
                    break

                current_node = current_node.next

            current_node.next = Node((key, value))

        if key not in self.keys:
            self.keys.append(key)
            self.count = len(self.keys)


    def hash_search(self, key):

        index = self.hash_func(key)

        try:

            if self.arr[index].value[0] == key:
                return self.arr[index].value[1]

            else:
                
                current_node = self.arr[index]

                while current_node.value[0] != key:
                    current_node = current_node.next

                return current_node.value[1]

        except ValueError or TypeError:
            raise Exception("Provided key has no paired value within 'hashmap' object.")


    def hash_delete(self, key):
        
        index = self.hash_func(key)

        try:
            self.keys.remove(key)
            self.count = len(self.keys)

            if self.arr[index].value[0] == key:
                self.arr[index] = None

            else:
                    
                current_node = self.arr[index]

                while current_node.next.value[0] != key:
                    current_node = current_node.next

                current_node.next = None
        
        except ValueError or TypeError:
            raise Exception("Provided key has no paired value within 'hashmap' object.")


    def __iter__(self):
        return hash_iter(self.keys)


test = hashmap(range(20))
