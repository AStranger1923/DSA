import numpy as np
from abc import ABC, abstractmethod

# Define the abstract class DSAQueue 
class DSAQueue(ABC):
    def __init__(self, capacity=100):
        self.queue = np.empty(capacity, dtype=object)  # Array to store elements of the queue using numpy
        self.count = 0  # Number of elements in the queue
        self.start = 0  # Index of the first element in the queue
        self.end = 0  # Index of the last element in the queue
        self.default_capacity = capacity  # Default capacity of the queue

    # Get the number of elements in the queue
    def get_count(self):
        return self.count

    # Check if the queue is empty
    def is_empty(self):
        return self.count == 0

    # Check if the queue is full
    def is_full(self):
        return self.count == len(self.queue)

    # Get the string representation of the queue
    def __str__(self):
        char_list = ""  # String to store characters
        i = self.start
        
        # Iterate through the queue
        while i != self.end:
            if self.queue[i] is not None:
                value = str(self.queue[i])  # Convert value to string
                for c in value:  # Convert each character manually
                    char_list += c
                char_list += ' '  # Append space
            i = (i + 1) % len(self.queue)
        
        return char_list  # Construct a string from the list

    @abstractmethod
    def peek(self):
        """Get the element at the front of the queue"""
        pass

    @abstractmethod
    def enqueue(self, value):
        """Add an element to the back of the queue"""
        pass

    @abstractmethod
    def dequeue(self):
        """Remove and return the element at the front of the queue"""
        pass


