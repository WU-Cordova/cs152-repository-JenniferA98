from typing import Any

from datastructures.array import Array
from datastructures.iqueue import IQueue, T

class CircularQueue(IQueue[T]):
    """ Represents a fixed-size circular queue. The queue
        is circular in the sense that the front and rear pointers wrap around the
        array when they reach the end. The queue is full when the rear pointer is
        one position behind the front pointer. The queue is empty when the front
        and rear pointers are equal. This implementation uses a fixed-size array.
    """

    def __init__(self, maxsize: int = 0, data_type=object) -> None:
        ''' Initializes the CircularQueue object with a maxsize and data_type.
        
            Arguments:
                maxsize: The maximum size of the queue
                data_type: The type of the elements in the queue
        '''
        self._maxsize = maxsize
        self._data_type = data_type
        self.circularqueue = Array([data_type()]* maxsize, data_type )
        self._front = 0
        self._rear = 0
        self._size = 0 
        


    def enqueue(self, item: T) -> None:
        ''' Adds an item to the rear of the queue

            Examples:
                >>> q = CircularQueue(maxsize=5, data_type=int)
                >>> q.enqueue(1)
                >>> q.enqueue(2)
                >>> q.enqueue(3)
                >>> q.front
                1
                >>> q.rear
                3
                >>> q.enqueue(4)
                >>> q.enqueue(5)
                >>> q.full
                True
                >>> q.enqueue(6)
                IndexError('Queue is full')
            
            Arguments:
                item: The item to add to the queue
                
            Raises:
                IndexError: If the queue is full
        '''
        if self.full:
            raise IndexError("Queue is full.")
        self.circularqueue[self._rear] = item
        self._rear = (self._rear + 1) % self._maxsize
        self._size += 1
    
        
            

    def dequeue(self) -> T:
        ''' Removes and returns the item at the front of the queue

            Examples:
                >>> q = CircularQueue(maxsize=5, data_type=int)
                >>> q.enqueue(1)
                >>> q.enqueue(2)
                >>> q.enqueue(3)
                >>> q.dequeue()
                1
                >>> q.dequeue()
                2
                >>> q.dequeue()
                3
                >>> q.dequeue()
                IndexError('Queue is empty')
                >>> q.dequeue()
                IndexError('Queue is empty')

            Returns:
                The item at the front of the queue

            Raises:
                IndexError: If the queue is empty
        '''
        if self.empty:
            raise IndexError ("Queue is empty")
        item = self.circularqueue[self._front]
        self._front = (self._front + 1) % self._maxsize
        self._size -= 1
        return item


    def clear(self) -> None:
        ''' Removes all items from the queue '''
        self._front = 0
        self._rear = 0
        self.circularqueue = Array([self._data_type()]*self._maxsize, self._data_type)


    @property
    def front(self) -> T:
        ''' Returns the item at the front of the queue without removing it

            Returns:
                The item at the front of the queue

            Raises:
                IndexError: If the queue is empty
        '''
        if self.empty:
            raise IndexError("Queue is empty")
        return self.circularqueue[self._front]

    @property
    def full(self) -> bool:
        ''' Returns True if the queue is full, False otherwise 
        
            Returns:
                True if the queue is full, False otherwise
        '''
        return self._size == self._maxsize

    @property
    def empty(self) -> bool:
        ''' Returns True if the queue is empty, False otherwise
        
            Returns:
                True if the queue is empty, False otherwise
        '''
        return self._front == self._rear
        
    
    @property
    def maxsize(self) -> int:
        ''' Returns the maximum size of the queue
        
            Returns:
                The maximum size of the queue
        '''
        return self._maxsize

    def __eq__(self, other: object) -> bool:
        ''' Returns True if this CircularQueue is equal to another object, False otherwise
        
            Equality is defined as:
                - The front and rear pointers are equal
                - The elements between the front and rear pointers are equal, even if they are in different positions
                
            Arguments:
                other: The object to compare this CircularQueue to
                
            Returns:
                True if this CircularQueue is equal to another object, False otherwise
        '''
        if not isinstance(other, CircularQueue):
            return False
    

        if self.__len__() != len(other):
            return False

        self_elements = [self.circularqueue[(self._front + i) % self._maxsize] for i in range(self.__len__())]
        other_elements = [other.circularqueue[(other._front + i) % other._maxsize] for i in range(len(other))]

        return sorted(self_elements) == sorted(other_elements)

    
    def __len__(self) -> int:
        ''' Returns the number of items in the queue
        
            Returns:
                The number of items in the queue
        '''
        return self._size

    def __str__(self) -> str:
        ''' Returns a string representation of the CircularQueue
        
            Returns:
                A string representation of the queue
        '''
        return str(self.circularqueue)

    def __repr__(self) -> str:
        ''' Returns a developer string representation of the CircularQueue object
        
            Returns:
                A string representation of the CircularQueue object
        '''
        return f'ArrayQueue({repr(self.circularqueue)})'
                                  
