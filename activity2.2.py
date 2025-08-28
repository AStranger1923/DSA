
from DSAQueue import *
from datetime import datetime

# Define the ShufflingQueue class that extends DSAQueue
class ShufflingQueue(DSAQueue):
    
    # Default constructor initializing the queue with a default capacity
    def __init__(self, capacity=100):
        super().__init__(capacity)
    
    # Retrieves the front element of the queue without removing it
    def peek(self):
        if self.is_empty():
            raise ValueError("Queue is empty.")
        return self.queue[0]  # Return the front element of the queue
    
    # Adds a new element to the end of the queue
    def enqueue(self, value):
        if self.is_full():
            raise ValueError("Queue is full.")
        self.queue[self.count] = value  # Place the new element at the end
        self.count += 1
        print(f"Enqueued: {value} at {datetime.now()}")

    # Removes and returns the front element of the queue
    def dequeue(self):
        if self.is_empty():
            raise ValueError("Queue is empty.")
        
        front_val = self.peek()  # Retrieve the front element
        
        # Shift all elements one position to the left (O(n) time complexity)
        # This effectively removes the front element
        for i in range(self.count - 1):
            self.queue[i] = self.queue[i + 1]
        
        # Set the last element to None
        self.queue[self.count - 1] = None
        self.count -= 1  # Decrease the count
        print(f"Dequeued: {front_val} at {datetime.now()}")
        
        return front_val

# Example usage
if __name__ == "__main__":
    # Create a new ShufflingQueue with a capacity of 5
    queue = ShufflingQueue(5)
    
    # Enqueue elements into the queue
    print("Enqueueing elements:")
    queue.enqueue("Alice")
    queue.enqueue("Bob")
    queue.enqueue("Charlie")
    queue.enqueue("Diana")
    queue.enqueue("Edward")
    
    # Display the front element of the queue
    print("\nPeek:", queue.peek())
    
    # The elements will be dequeued in the order they were enqueued
    print("\nDequeuing elements:")
    while not queue.is_empty():
        print(queue.dequeue())
    
    # Attempt to dequeue from an empty queue (this will throw an exception)
    try:
        queue.dequeue()
    except ValueError as e:
        print("\nException caught:", e)
