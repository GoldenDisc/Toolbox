
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


class binaryTree():    # Fix bug where 'None' becomes the value of a node rather than an empty space.

    def __init__(self, treeArr, index=0, isRoot=True):

        if isRoot:

            self.root = binaryNode(treeArr[1])

            self.root.left = self.__init__(treeArr, 2, False)
            self.root.right = self.__init__(treeArr, 3, False)

        else:

            try:
                current_node = binaryNode(treeArr[index])

                current_node.left = self.__init__(treeArr, index * 2, False)
                current_node.right = self.__init__(treeArr, index * 2 + 1, False)

                return current_node

            except IndexError:
                return None


def treeSum(node):
    """
    Takes the sum of a section of a binary tree containing only floats and integers.

    Arguments:
        node (binaryNode): The root head of the branch to be counted. The sum of this node and all subsequent nodes will be taken.

    Returns:
        float: The sum of every node on the given section of the tree.

    Raises:
        Exception: A custom exception is raised if any of the nodes of the given section of the tree cotain anything other than a 
            float or integer.
    """

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
    """
    Adds or replaces a binary node on a binary tree.

    Arguments:
        parent (binaryNode): The node of a binary tree that will have one of its child nodes replaced.

        direction (str): Either 'left' or 'right,' determines which of the parent's nodes is replaced. 

        value (no designated type): Can be of any data type. Whatever data is added will be held in a 'binaryNode' object and 
            replaces the given parent node's left or right child node. This is with the exception that the given value is either a
            'Node' or 'binaryNode' object, in which case the value of the object will be copied over to form a new object, rather 
            than the object itself.

    Raises:
        Exception: A custom exception is rasied if the 'direction' argument given isn't a string containing the words 'left' or 'right.'

    Notes:
        This function is written for the purpose of adding leaf nodes to trees, in which case the node being replaced by this function
            would simply be the value 'None' rather than a node object. Keep in mind that this function can overwrite a parent node's 
            children, and will not maintain further relationships in such cases. This does, however, add the extra functionality of 
            easily removing entire branches from a tree if a specific node is replaced.
    """

    direction = direction.lower()

    if direction != "left" and direction != "right":
        raise Exception("The direction given to the 'addBinaryNode' function must be either 'left' or 'right.' ")

    elif isinstance(value, Node) or isinstance(value, binaryNode):

        if direction == "left":
            parent.left = binaryNode(value.value)
        else:
            parent.right = binaryNode(value.value)

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


def convertToTree(arr, direction='left'):
    
    index = 1
    treeList = [None, ]
    treeDict = {}

    for value in arr:

        treeDict[index] = value

        if direction == "left":
            index = index * 2

        elif direction == "right":
            index = index * 2 + 1

    for num in range(1, (list(treeDict)[-1] + 1)):


        try:
           treeList.append(treeDict[num]) 
        except KeyError:
            treeList.append(None)

    return binaryTree(treeList)
        

test_list = ["root", "left", "left2", "left3", "left4", "left5"]

tree = convertToTree(test_list)

print(tree.root.right)
