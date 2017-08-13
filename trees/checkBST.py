import sys
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def isBST(root,max,min):
    if root==None:
        return True
    if root.data<=min or root.data>=max:
        return False
    return isBST(root.left,root.data,min) and isBST(root.right,max,root.data)

root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)

if (isBST(root,sys.maxint,-sys.maxint-1)):
    print "Is BST"
else:
    print "Not a BST"
