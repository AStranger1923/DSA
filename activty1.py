

import time
from DSAStack import *
import numpy as np  # Add numpy import

if __name__ == "__main__":
    stack = DSAStack()
    elements = np.array([1, 2, 3, 4, 5, 6, 7])  # Use numpy array instead of list
    
    start_push = time.time()
    for element in elements:
        stack.push(element)
        print(f"Pushed element: {element}")
    end_push = time.time()
    print(f"\nTime taken to push elements: {end_push - start_push:.6f} seconds")
    
    print("\nStack Details:")
    print(f"Count: {stack.get_count()}")
    print(f"Is Empty: {stack.is_empty()}")
    print(f"Is Full: {stack.is_full()}")
    print(f"Top element: {stack.top()}")
    
    print("\nPopping elements from the stack:")
    try:
        while not stack.is_empty():
            print(f"Popped element: {stack.pop()}")
        
        # Attempt to pop from an empty stack
        print(f"Popped element: {stack.pop()}")
    except IndexError as e:
        print(f"Error: {e}")
