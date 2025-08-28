import numpy as np

class DSAStack:
    DEFAULT_CAPACITY = 5  # Default capacity of the stack

    def __init__(self, max_capacity=DEFAULT_CAPACITY):
        """Default and alternative constructor"""
        self.stack = np.empty(max_capacity, dtype=object)  # Allocating stack with given capacity using numpy array
        self.count = 0  # Initialize count to 0
        self.max_capacity = max_capacity

    def get_count(self):
        """Get the count of the stack"""
        return self.count

    def is_empty(self):
        """Check if the stack is empty"""
        return self.count == 0

    def is_full(self):
        """Check if the stack is full"""
        return self.count >= self.max_capacity

    def top(self):
        """Get the top value from the stack"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.stack[self.count - 1]  # Return top value

    def push(self, x):
        """Push value to the stack"""
        if self.is_full():
            print("Stack is full")
            return
        self.stack[self.count] = x  # Push value to stack
        self.count += 1  # Increment count

    def pop(self):
        """Pop value from the stack"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        value = self.stack[self.count - 1]  # Get value to be popped
        self.stack[self.count - 1] = None  # Set value to None
        self.count -= 1  # Decrement count
        return value  # Return popped value
