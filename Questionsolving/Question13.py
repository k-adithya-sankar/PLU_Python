#Search in Singly Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

key = 20

temp = head
found = False

while temp:
    if temp.data == key:
        found = True
        break
    temp = temp.next

print(found)