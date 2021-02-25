
class Node():

    def __init__(self, value):

        self.value = value
        self.next = None
        self.back = None


class linkedList():

    def __init__(self, valueList):

        nodeList = []

        for item in valueList:
            nodeList.append(Node(item))

        for index, node in enumerate(nodeList):

            if node != nodeList[-1]:
                node.next = nodeList[index + 1]

            if index != 0:
                node.back = nodeList[index - 1]

        
        self.head = nodeList[0]
        self.rear = nodeList[-1]

    
    def addNode(self, value):
        self.rear.next = Node(value)
        self.rear = self.rear.next

    
    def removeNode(self, value):
        
        node = self.head

        while node != None:
            
            if node.value == value:

                if node.next != None and node.back != None:
                    node.back.next = node.next
                    node.next.back = node.back
                
                elif node.next == None:
                    node.back.next = None

                elif node.back == None:
                    node.next.back = None

                
                if node == self.head:
                    self.head = node.next
                
                elif node == self.rear:
                    self.rear = node.back


                del node

                break

            node = node.next


    def removeAllNodes(self, value):
        
        node = self.head

        while node != None:
            
            del_node = node
            node = node.next

            if del_node.value == value:

                if del_node.next != None and del_node.back != None:
                    del_node.back.next = del_node.next
                    del_node.next.back = del_node.back
                
                elif del_node.next == None:
                    del_node.back.next = None

                elif del_node.back == None:
                    del_node.next.back = None

                
                if del_node == self.head:
                    self.head = del_node.next
                
                elif del_node == self.rear:
                    self.rear = del_node.back


                del del_node


    def countNodes(self):

        count = 0
        node = self.head

        while node != None:

            count += 1
            node = node.next

        return count 
