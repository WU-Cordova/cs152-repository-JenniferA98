from __future__ import annotations

from dataclasses import dataclass
import os
from typing import Optional, Sequence
from datastructures.ilinkedlist import ILinkedList, T


class LinkedList[T](ILinkedList[T]):

    @dataclass
    class Node:
        data: T
        next: Optional[LinkedList.Node] = None
        previous: Optional[LinkedList.Node] = None

    def __init__(self, data_type: type = object) -> None:
        self._data_type = data_type
        self._head : Optional[LinkedList.Node] = None
        self._tail : Optional[LinkedList.Node] = None
        self.size = 0
        self._iterator_node: Optional[LinkedList.Node] = None

    @staticmethod
    def from_sequence(sequence: Sequence[T], data_type: type=object) -> LinkedList[T]:
        """Returns linked list populated by sequence"""
        new_list = LinkedList(data_type = data_type)

        for item in sequence:
            if not isinstance(item, data_type):
                raise TypeError("Item is not of type {self.data_type}")
            new_list.append(item)

        return new_list

    def append(self, item: T) -> None:
        if not isinstance(item, self._data_type):
            raise TypeError("Data type must be of type {self.data_type}.")
        
        new_node = LinkedList.Node(item)

        if self._head is None:
            self._head = self._tail = new_node
        else:
            if self._tail is not None:
                self._tail.next= new_node
                new_node.previous = self._tail
                self._tail = new_node

        self.size += 1

    def prepend(self, item: T) -> None:
        if not isinstance(item, self._data_type):
            raise TypeError("Data type must be of type {self.data_type}.")
        
        new_node = LinkedList.Node(item)

        if self._head is None:
            self._head = self._tail = new_node

        else:
            new_node.next = self._head
            self._head.previous = new_node
            self._head = new_node
        
        self.size += 1

    def insert_before(self, target: T, item: T) -> None:
        raise NotImplementedError("LinkedList.insert_before is not implemented")

    def insert_after(self, target: T, item: T) -> None:
        raise NotImplementedError("LinkedList.insert_after is not implemented")

    def remove(self, item: T) -> None:
        raise NotImplementedError("LinkedList.remove is not implemented")

    def remove_all(self, item: T) -> None:
        raise NotImplementedError("LinkedList.remove_all is not implemented")

    def pop(self) -> T:
        raise NotImplementedError("LinkedList.pop is not implemented")

    def pop_front(self) -> T:
        raise NotImplementedError("LinkedList.pop_front is not implemented")

    @property
    def front(self) -> T:
        raise NotImplementedError("LinkedList.front is not implemented")

    @property
    def back(self) -> T:
        if self._tail is None:
            raise IndexError("List is empty")
        return self._tail

    @property
    def empty(self) -> bool:
        return self.size == 0

    def __len__(self) -> int:
        return self.size

    def clear(self) -> None:
        for 

    def __contains__(self, item: T) -> bool:
        raise NotImplementedError("LinkedList.__contains__ is not implemented")

    def __iter__(self) -> ILinkedList[T]:
        raise NotImplementedError("LinkedList.__iter__ is not implemented")

    def __next__(self) -> T:
        raise NotImplementedError("LinkedList.__next__ is not implemented")
    
    def __reversed__(self) -> ILinkedList[T]:
        raise NotImplementedError("LinkedList.__reversed__ is not implemented")
    
    def __eq__(self, other: object) -> bool:
        raise NotImplementedError("LinkedList.__eq__ is not implemented")

    def __str__(self) -> str:
        items = []
        current = self.head
        while current:
            items.append(repr(current.data))
            current = current.next
        return '[' + ', '.join(items) + ']'

    def __repr__(self) -> str:
        items = []
        current = self.head
        while current:
            items.append(repr(current.data))
            current = current.next
        return f"LinkedList({' <-> '.join(items)}) Count: {self.count}"


if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'OOPS!\nThis is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')
