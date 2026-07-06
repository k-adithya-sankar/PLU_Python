'''SECTION B
-------------------------'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linked_list:
    def __init__(self):
        self.head=None
    def insert(self,data):
        newnode=Node(data)
        newnode.next=self.head
        self.head=newnode
    def inbet(self,data,value):
        newnode=Node(data)
        temp=self.head
        while temp.next:
            if temp.next.data==value:
                newnode.next=temp.next
                temp.next=newnode
                break
            temp=temp.next
    def delbet(self,value):
        temp=self.head
        while temp.next:
            if temp.next.data==value:
                temp.next=temp.next.next
                break
            temp=temp.next
    def count(self):
        temp=self.head
        count=0
        while temp:
            count+=1
            temp=temp.next
        print(count)
    def dis(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next
l=Linked_list()
l.insert(50)
l.insert(40)
l.insert(30)
l.insert(20)
l.insert(10)
l.dis()
print("\n")
l.inbet(25,30)
l.dis()
print("\n")
l.delbet(30)
l.dis()
print("\n")
l.count()