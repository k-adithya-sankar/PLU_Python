class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
def leaf(root):
    if root is None:
        return
    # leaf(root.right)
    # leaf(root.left)
    print(root.left.data)
    print(root.right.data)
root=Node(50)
root.right=Node(70)
root.left=Node(30)
leaf(root)