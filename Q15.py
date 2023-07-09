class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue.pop(0)

    def front(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue[0]

    def size(self):
        return len(self.queue)
