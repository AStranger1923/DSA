
from DSAQueue import *
from datetime import datetime as timestamp
# Define the CircularQueue class that extends DSAQueue
class CircularQueue(DSAQueue):
    
    # Default constructor initializing the queue with a default capacity
    def __init__(self, capacity=100):
        super().__init__(capacity)
    
    # Retrieves the front element of the queue without removing it
    def peek(self):
        if self.is_empty():
            raise ValueError("Queue empty.")
        return self.queue[self.start]
    
    # Adds a new element to the end of the queue
    def enqueue(self, value):
        if self.is_full():
            raise ValueError("Queue full.")
        self.queue[self.end] = value
        self.end = (self.end + 1) % len(self.queue)  # Circular increment
        self.count += 1
        print(f"Enqueued: {value} at {timestamp.now()}")
    
    # Removes and returns the front element of the queue
    def dequeue(self):
        if self.is_empty():
            raise ValueError("Queue empty.")
        
        value = self.queue[self.start]
        self.queue[self.start] = None
        self.start = (self.start + 1) % len(self.queue)  # Circular increment
        self.count -= 1
        print(f"Dequeued: {value} at {timestamp.now()}")
        return value

# Example usage
if __name__ == "__main__":
    queue = CircularQueue(5)
    
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    
    print("Front element:", queue.peek())  # Should print 1
    print("Dequeue:", queue.dequeue())  # Should print 1
    print("Dequeue:", queue.dequeue())  # Should print 2
    
    queue.enqueue(6)
    queue.enqueue(7)
    
    print("Front element:", queue.peek())  # Should print 3
