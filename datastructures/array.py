# datastructures.array.Array

""" This module defines an Array class that represents a one-dimensional array. 
    See the stipulations in iarray.py for more information on the methods and their expected behavior.
    Methods that are not implemented raise a NotImplementedError until they are implemented.
"""

from __future__ import annotations
from collections.abc import Sequence
import os
from typing import Any, Iterator, overload
import numpy as np
from numpy.typing import NDArray


from datastructures.iarray import IArray, T


class Array(IArray[T]):  

    def __init__(self, starting_sequence: Sequence[T]=[], data_type: type=object) -> None: 
        
        self.starting_sequence= starting_sequence
        
        if not all(isinstance(item, data_type) for item in starting_sequence):
            raise TypeError(f"All elements must be of type {data_type}")
        self._data = np.array(starting_sequence, dtype = data_type)
        self._logical_size = len(starting_sequence)
        self._physical_size = self._data.size

    @overload
    def __getitem__(self, index: int) -> T: ...
    @overload
    def __getitem__(self, index: slice) -> Sequence[T]: ...
    def __getitem__(self, index: int | slice) -> T | Sequence[T]:

        if isinstance(index, int):
            if index < 0:
                index += self._logical_size
            if index < 0 or index >= self._logical_size:
                raise IndexError("Index out of bounds")
            return self._data[index]
        
        elif isinstance(index, slice):
            start = index.start if index.start is not None else 0
            stop = index.stop if index.stop is not None else self._logical_size
            step = index.step if index.step is not None else 1

            if start < 0 or stop > self._logical_size or step == 0:
                raise IndexError("Index out of bounds")

            returns = self._data[start:stop:step]
            return Array(starting_sequence=returns.tolist(), data_type=self.__data_type)
  
  
    def __setitem__(self, index: int, item: T) -> None:

        if index < 0:
            index += self._logical_size
        if index < 0 or index >= self._logical_size:
            raise IndexError("Index out of bounds")
        if not isinstance(item, self._data.dtype.type):
            raise TypeError(f"Item must be of type {self._data.dtype}")
        
        self._data[index] = item

    def __grow(self, new_size:int) -> None:
        new_data = np.empty(new_size, dtype=self._data.dtype)

        new_data[:self._logical_size] = self._data

        self._data = new_data
        self._physical_size = new_size


    def append(self, data: T) -> None: ##NEEDS WORK
        if not isinstance(data, self._data.dtype.type) and self._data.size > 0:
            raise TypeError(f"Data must be of type {self._data.dtype}")
        
        if self._logical_size >= self._physical_size:
            new_size = self._physical_size * 2 if self._physical_size > 0 else 1
            self.__grow(new_size)

        self._data[self._logical_size] = data
        self._logical_size += 1


    def append_front(self, data: T) -> None:
        if not isinstance(data, self._data.dtype.type):
            raise TypeError(f"Data must be of type {self._data.dtype}")
        
        if self._logical_size >= self._physical_size:
            new_size = self._physical_size * 2 if self._physical_size > 0 else 1
            self.__grow(new_size)

        self._data[1:self._logical_size + 1] =self._data[:self._logical_size]
        self._data[0] = data
        self._logical_size += 1


    def __shrink(self, new_size:int):


        
    def pop(self) -> None:
        
    
    def pop_front(self) -> None:
        raise NotImplementedError('Pop front not implemented.')

    def __len__(self) -> int: 

        return self._logical_size



    def __eq__(self, other: object) -> bool:

        if not isinstance(other, Array):
            return False
        elif len(other) != self._logical_size:
            return False
        for i in range(len(self._data)):
            if self._data[i] != other[i]:
                return False
        return True
    
    def __iter__(self) -> Iterator[T]:
        return iter(self._data)
    
        

    def __reversed__(self) -> Iterator[T]:
        reversed_data = self._data[::-1]
        return iter(reversed_data)

    def __delitem__(self, index: int) -> None:
        raise NotImplementedError('Delete not implemented.')

    def __contains__(self, item: Any) -> bool:
        return any(x > item for x in self._data)
        

    def clear(self) -> None:
        raise NotImplementedError('Clear not implemented.')

    def __str__(self) -> str:
        return '[' + ', '.join(str(item) for item in self) + ']'
    
    def __repr__(self) -> str:
        return f'Array {self.__str__()}, Logical: {self.__item_count}, Physical: {len(self.__items)}, type: {self.__data_type}'
    

if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')