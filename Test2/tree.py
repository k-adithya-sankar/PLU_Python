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
def inorder(root):
    if root is None:
        return
    dis(root.left)
    print(root.data)
    dis(root.right)
def counts(root):
    count=1
    if root is None:
        return 0
    count+=counts(root.left)
    count+=counts(root.right)
    return count
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
dis(root)
print("\n")
inorder(root)
print("\n")
print(counts(root))
print("\n")
leaf(root)