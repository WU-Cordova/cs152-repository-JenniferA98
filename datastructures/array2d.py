from __future__ import annotations
import os
from typing import Iterator, Sequence

from datastructures.iarray import IArray
from datastructures.array import Array
from datastructures.iarray2d import IArray2D, T


class Array2D(IArray2D[T]):


    class Row(IArray2D.IRow[T]):
        def __init__(self, row_index: int, array: IArray, num_columns: int, data_type = type) -> None:

            self.row_index = row_index
            self.array = array
            self.num_columns = num_columns
            self.data_type = data_type

        def __getitem__(self, column_index: int) -> T:
            if column_index < 0 or column_index >= self.num_columns:
                raise IndexError("Column index out of bounds.")
            index = self.map_index(self.row_index, column_index)
            return self.array[index]
            
        
        def __setitem__(self, column_index: int, value: T) -> None:
            index = self.map_index(self.row_index, column_index)
            self.array[index] = value

        
        def map_index(self, row_index:int , column_index:int) -> int:
            return row_index * self.num_columns + column_index
        
        
        def __iter__(self) -> Iterator[T]:
            for column_index in range(self.num_columns):
                yield self[column_index]

        
        def __reversed__(self) -> Iterator[T]:
            for column_index in range(self.num_columns -1 ,-1, -1):
                yield self[column_index]

        def __len__(self) -> int:
            return self.num_columns
        
        def __str__(self) -> str:
            return f"[{', '.join([str(self[column_index]) for column_index in range(self.num_columns)])}]"
        
        def __repr__(self) -> str:
            return f'Row {self.row_index}: [{", ".join([str(self[column_index]) for column_index in range(self.num_columns - 1)])}, {str(self[self.num_columns - 1])}]'


    def __init__(self, starting_sequence: Sequence[Sequence[T]]=[[]], data_type=object) -> None:
        
        self.data_type = data_type
        if not isinstance(starting_sequence, (list, tuple)):
            raise ValueError("starting_sequence must be a sequence.")
        
        self.row_len = len(starting_sequence)
    
        if self.row_len == 0:
            self.column_len = 0
        else:
            first_row_len = len(starting_sequence[0])
            for row in starting_sequence:
                if not isinstance(row, (list,tuple)):
                    raise ValueError("Each row in starting_sequence must be a sequence.")
                if len(row) != first_row_len:
                    raise ValueError("All rows must have the same length.")
                
            self.column_len = first_row_len

        self.array2d = Array([data_type() for _ in range(self.row_len * self.column_len)],data_type=data_type)

        index = 0 
        for row_index in range(self.row_len):
            for column_index in range(self.column_len):
                self.array2d[index]= starting_sequence[row_index][column_index]
                index += 1



    @staticmethod
    def empty(rows: int=0, cols: int=0, data_type: type=object) -> Array2D:
        starting_sequence = [[data_type() for _ in range(cols)] for _ in range(rows)]
        return Array2D(starting_sequence, data_type=data_type)

    def __getitem__(self, row_index: int) -> Array2D.IRow[T]: 
        if row_index < 0  or row_index >= self.row_len:
            raise IndexError("Row index out of bounds.")
        
    
        return Array2D.Row(row_index, self.array2d, self.column_len, self.data_type)

    
    def __iter__(self) -> Iterator[Sequence[T]]: 
        for row_index in range(self.row_len):
            yield self[row_index]

    def __reversed__(self):
        for row_index in range(self.row_len - 1, -1, -1):
            yield self[row_index]

    def __len__(self): 
        return self.row_len
                        
    def __str__(self) -> str: 
        return f'[{", ".join(f"{str(row)}" for row in self)}]'
    
    def __repr__(self) -> str: 
        return f'Array2D {self.column_len} Rows x {self.row_len} Columns, items: {str(self)}'

    def __eq__(self, other:object) -> bool:
        if not isinstance(other, Array2D):
            return False
        
        if self.row_len != other.row_len or self.column_len != other.column_len:
            return False
        
        for row_index in range(self.row_len):
            for col_index in range(self.column_len):
                if self[row_index][col_index] != other[row_index][col_index]:
                    return False
                
        return True
 

    def set_border(self, value):
        """Time complexity = (col_len+ row_len)"""
        if self.row_len == 0 or self.column_len == 0:
            return
        for col in range(self.column_len):
            self[0][col] = value
            if self.row_len > 1:
                self[self.row_len - 1][col]= value
        
        for row in range(1, self.row_len-1):
            self[row][0] = value
            if self.column_len > 1:
                self[row][self.column_len - 1]= value

if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')