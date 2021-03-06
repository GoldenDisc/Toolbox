
# Linked Lists

class Node():
    """ """

    def __init__(self, value, next=None, back=None):

        self.value = value

        self.next = next
        self.back = back


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


def countNodes(node):

    count = 0

    while node != None:

        count += 1
        node = node.next

    return count 



# Binary Trees 

class binaryNode():

    def __init__(self, value, left=None, right=None):

        self.value = value

        self.left = left
        self.right = right


def treeCreator(arr):

    if len(arr) == 0:
        return None
            
    currentNode = binaryNode(arr[0])

    currentNode.left = treeCreator(arr[1])
    currentNode.right = treeCreator(arr[2])

    return currentNode


def treeSum(node):
    """Intakes a binary node, returns the sum of that node and all subsequent nodes as an integer. Raises an error if the provided node either isn't a binary node 
    or doesn't hold an integer value."""

    if not isinstance(node, binaryNode):
        raise Exception("The node given to the 'treeSum' function must be a binaryNode object.")

    if node == None:
        return 0

    elif isinstance(node.value, int) or isinstance(node.value, float):
            
        count = float(node.value) + treeSum(node.left) + treeSum(node.right)
        
        return count

    else:
        raise Exception("The value of all nodes in a binary tree given to the 'treeSum' function must be either integers or floats.")


def addBinaryNode(parent, direction, value):
    """Intakes a node, a directional string ('left' or 'right,') and a value. Replaces the given parent node's left or right child node with a node of the given value.
    This function is designed to be used to add leaf nodes, but can be used to replace entire branches of nodes. Note that the new child node has no children of its own, 
    and that if the new node is replacing another, the children of the old node will no longer be connected to the tree."""

    if direction != "left" and direction != "right":
        raise Exception("The direction given to the 'addBinaryNode' function must be either 'left' or 'right,' given all lowercase as typed here.")


    if isinstance(value, binaryNode):

        if direction == "left":
            parent.left = value
        else:
            parent.right = value

    else:

        if direction == "left":
            parent.left = binaryNode(value)
        else:
            parent.right = binaryNode(value)


def convertToLinkedList(arr):

    arrValues = []

    for node in arr:
        arrValues.append(node.value)

    return linkedList(treeValues)


def convertToTree(arr, dir=2):
    """
    Converts an array into a binary tree.

    Arguments:
        arr (list): The array to be converted into a binary tree.

        dir (int, optional): represents the direction each node holdng each given value will be placed. 1 represents left, 2 represents right.
            Every value in the list will have the value after it placed as either its left or right node, the given integer determines which.

    Returns:
        binaryTree: the binary tree version of the given array.
    """

    if isinstance(arr, linkedList):

        node = arr.head
        linked_values = []

        while node != None:
            linked_values.append(node.value)

            node = node.next

        arr = linked_values

    treeList = [arr[0], [], []]
    tempList = treeList[dir]

    for item in arr[1:]:
        
        tempList.append(item)

        tempList.append([])
        tempList.append([])

        tempList = tempList[dir]

    print(treeList)
    return binaryTree(treeList)
    

class binaryTree():

    def __init__(self, treeArray):

        self.root = Node(treeArray[0])

        self.root.left = treeCreator(treeArray[1])
        self.root.right = treeCreator(treeArray[2])

print(convertToTree.__doc__)
