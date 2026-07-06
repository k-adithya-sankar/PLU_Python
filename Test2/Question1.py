class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linked_list:
    def __init__(self):
        self.head=None
l=Linked_list()
l.insert(50)
l.insert(40)
l.insert(30)
l.insert(20)
l.insert(10)
l.dis()
print("\n")