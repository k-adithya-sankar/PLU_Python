class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data)
    inorder(root.right)
root=Node(50)
root.right=Node(70)
root.left=Node(30)
inorder(root)