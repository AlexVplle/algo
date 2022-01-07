class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if data <= self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)

def treeSort(array):
    """Complexity : O(n**2)"""
    if len(array) == 0:
        return array
    root = Node(array[0])
    for i in array[1:]:
        root.insert(i) 
    res = []
    inorder(root,res)
    return res
    
def inorder(root, res):
    if root:
        inorder(root.left,res)
        res.append(root.data)
        inorder(root.right,res)


