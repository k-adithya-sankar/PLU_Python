#Delete Last Item in Singly Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

temp = head

while temp.next.next:
    temp = temp.next

temp.next = None

temp = head

while temp:
    print(temp.data)
    temp = temp.next