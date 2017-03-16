class Node:  
    def __init__(self, value=None, left=None, right=None):  
        self.value = value  
        self.left = left  
        self.right = right  

def preTraverse(root):  
    if root==None:  
        return  
    print(root.value)  
    preTraverse(root.left)  
    preTraverse(root.right)  
  
def midTraverse(root):  
    if root==None:  
        return  
    midTraverse(root.left)  
    print(root.value)  
    midTraverse(root.right)  
  
def afterTraverse(root):  
    if root==None:  
        return  
    afterTraverse(root.left)  
    afterTraverse(root.right)  
    print(root.value)  

tree = Node('D',Node('B',Node('A'),Node('C')),Node('E',right=Node('G',Node('F'))))
preTraverse(tree)
