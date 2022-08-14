from queue import Queue, PriorityQueue
from collections import deque

class StateBuffer:
    def __init__(self, buffer):
        self.buffer = buffer
    
    def add(self, state):
        raise NotImplementedError()
    
    def pop(self):
        raise NotImplementedError()
    
    def size(self):
        raise NotImplementedError()

class QueueBuffer(StateBuffer):
    def __init__(self):
        super().__init__(Queue())
    
    def add(self, state):
        self.buffer.put(state)
    
    def pop(self):
        return self.buffer.get()
    
    def size(self):
        return self.buffer.qsize()

class StackBuffer(StateBuffer):
    def __init__(self):
        super().__init__(deque())
    
    def add(self, state):
        self.buffer.append(state)
    
    def pop(self):
        return self.buffer.pop()
    
    def size(self):
        return self.buffer.__len__()

class PriorityQueueBuffer(StateBuffer):
    def __init__(self):
        super().__init__(PriorityQueue())
    
    def add(self, state):
        self.buffer.put(state)
    
    def pop(self):
        return self.buffer.get()
    
    def size(self):
        return self.buffer.qsize()