# Queue Data Structure

class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue is Empty")
        else:
            print(self.queue.pop(0))

q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.queue)

q.dequeue()

print(q.queue)