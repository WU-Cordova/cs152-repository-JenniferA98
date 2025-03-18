import os

from datastructures.array import Array, T
from datastructures.istack import IStack

class ArrayStack(IStack[T]):
    ''' ArrayStack class that implements the IStack interface. The ArrayStack is a 
        fixed-size stack that uses an Array to store the items.'''
    
    def __init__(self, max_size: int = 0, data_type=object) -> None:
        ''' Constructor to initialize the stack 
        
            Arguments: 
                max_size: int -- The maximum size of the stack. 
                data_type: type -- The data type of the stack.       
        '''
        if max_size <= 0:
            raise ValueError("Max size must be greater than 0.")
        self.max_size = max_size
        self.data_type = data_type
        self._top  = 0
        self.stack = Array([None]* max_size, data_type)

    def push(self, item: T) -> None:
        "Add item on top"
        if self.full:
            raise OverflowError("Stack if full.")
        self.stack[self._top] = item
        self._top += 1

    def pop(self) -> T:
       "Removes and return top item"
       if self.empty:
           raise IndexError("Stack is empty.")
       self._top -= 1
       return self.stack[self._top]

    def clear(self) -> None:
       "Clears stack"
       self.stack = Array([None] * self.max_size, self.data_type)
       self._top = 0
    @property
    def peek(self) -> T:
       "Returns top item without removing it."
       if self.empty:
           raise IndexError("Stack is empty.")
       return self.stack[self._top - 1]


    @property
    def maxsize(self) -> int:
        ''' Returns the maximum size of the stack. 
        
            Returns:
                int: The maximum size of the stack.
        '''
        return self.max_size
    
    @property
    def full(self) -> bool:
        ''' Returns True if the stack is full, False otherwise. 
        
            Returns:
                bool: True if the stack is full, False otherwise.
        '''
        return self._top == self.max_size

    @property
    def empty(self) -> bool:
        return self._top == 0

    def __eq__(self, other: object) -> bool:
        "Checks for stack equality in terms of size and values."
        if not isinstance(other, ArrayStack) or len(self) != len(other):
           return False
        return all(self.stack[i] == other.stack[i] for i in range(len(self)))

    def __len__(self) -> int:
       "Returns size of stack."
       return self._top
    
    def __contains__(self, item: T) -> bool:
       "Checks if an items exists in stack."
       return item in self.stack[:self._top]
    def __str__(self) -> str:
        return str([self.stack[i] for i in range(self._top)])
    
    def __repr__(self) -> str:
        return f"ArrayStack({self.maxsize}): items: {str(self)}"
    
if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'OOPS!\nThis is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')

