from LinkedListAndTree import Node


def alph_int(char):
    return ord(char.lower()) - 96


class hashmap:
    
    def __init__(self):
        
        self.arr = [Node(None) for x in range(10)]


    def hash_func(self, key):
        return (alph_int(key[0]) * alph_int(key[-1]) * len(key)) % len(self.arr)


    def hash_insert(self, key, value, index=None):

        if index == None:
            index = self.hash_func(key)


        if self.arr[index] == None:
            self.arr[index] = (key, value)

        else:

            try:
                self.hash_insert(key, value, index + len(key) // 2)

            except IndexError:
                self.hash_insert(key, value, len(key) // 2)




test_dict = hashmap()
