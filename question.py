class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inOrderTraverse(head):
    if head.left:
        inOrderTraverse(head.left)
    print(head.data)
    if head.right:
        inOrderTraverse(head.right)
    return

aNode = Node("a")
bNode = Node("b")
cNode = Node("c")
dNode = Node("d")
eNode = Node("e")
fNode = Node("f")
gNode = Node("g")

aNode.left = bNode
aNode.right = cNode
bNode.left = dNode
bNode.right = eNode
cNode.left = fNode
cNode.right = gNode

inOrderTraverse(aNode)
