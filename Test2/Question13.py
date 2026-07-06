class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
def dis(root):
    if root is None:
        return
    print(root.data)
    dis(root.right)
    dis(root.left)
root=Node(50)
root.right=Node(70)
root.left=Node(30)
dis(root)