class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
def counts(root):
    count=1
    if root is None:
        return 0
    count+=counts(root.left)
    count+=counts(root.right)
    return count
root=Node(50)
root.right=Node(70)
root.left=Node(30)
print(counts(root))
