#Access by Index in Singly Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

index = 1

temp = head
count = 0

while temp:
    if count == index:
        print(temp.data)
        break

    count += 1
    temp = temp.next