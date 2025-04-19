from __future__ import annotations

from dataclasses import dataclass
import os
from typing import Optional, Sequence
from datastructures.ilinkedlist import ILinkedList, T

class LinkedList(ILinkedList[T]):

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
        """Appends items of same type to the end."""
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
        """Appends items of the same type to the front."""
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
        if not isinstance(item, self._data_type) or not isinstance(target, self._data_type):
            raise TypeError("Both item and target must be of type {}".format(self._data_type))

        current = self._head
        while current:
            if current.data == target:
                new_node = LinkedList.Node(item, next=current, previous=current.previous)
                if current.previous:
                    current.previous.next = new_node
                else:
                    self._head = new_node
                current.previous = new_node
                self.size += 1
                return
            current = current.next
        raise ValueError(f"{target} not found in the list")

    def insert_after(self, target: T, item: T) -> None:
        if not isinstance(item, self._data_type) or not isinstance(target, self._data_type):
            raise TypeError("Both item and target must be of type {}".format(self._data_type))

        current = self._head
        while current:
            if current.data == target:
                new_node = LinkedList.Node(item, next=current.next, previous=current)
                if current.next:
                    current.next.previous = new_node
                else:
                    self._tail = new_node
                current.next = new_node
                self.size += 1
                return
            current = current.next
        raise ValueError(f"{target} not found in the list")

    def remove(self, item: T) -> None:
        if not isinstance(item, self._data_type):
            raise TypeError(f"Item must be of type {self._data_type.__name__}")

        current = self._head
        while current is not None:
            if current.data == item:
                if current.previous is None and current.next is None:
                    self._head = None
                    self._tail = None
                elif current.previous is None:
                        self._head = current.next
                        if self._head:
                            self._head.previous = None
                elif current.next is None:
                    self._tail = current.previous
                    if self._tail:
                        self._tail.next = None
                else:
                    current.previous.next = current.next
                    current.next.previous = current.previous
                return
            current = current.next
            self.size -= 1

        raise ValueError(f"{item} not found in the list")

    def remove_all(self, item: T) -> None:
        if not isinstance(item, self._data_type):
            raise TypeError("Item must be of type {}".format(self._data_type))

        current = self._head
        found = False
        while current:
            next_node = current.next
            if current.data == item:
                found = True
                if current.previous:
                    current.previous.next = current.next
                else:
                    self._head = current.next

                if current.next:
                    current.next.previous = current.previous
                else:
                    self._tail = current.previous

                self.size -= 1
            current = next_node

        if not found:
            raise ValueError(f"{item} not found in list.")

    def pop(self) -> T:
        if self._tail is None:
            raise IndexError("List is empty.")
        data = self._tail.data
        if self._tail.previous:
            self._tail = self._tail.previous
            self._tail.next = None
        else:
            self._head = self._tail = None

        self.size -= 1
        return data

    def pop_front(self) -> T:
        if self._head is None:
            raise IndexError("Pop from empty list")

        data = self._head.data
        if self._head.next:
            self._head = self._head.next
            self._head.previous = None
        else:
            self._head = self._tail = None

        self.size -= 1
        return data

    @property
    def front(self) -> T:
        if self._head is None:
            raise IndexError("List is empty.")
        return self._head.data

    @property
    def back(self) -> T:
        if self._tail is None:
            raise IndexError("List is empty")
        return self._tail.data

    @property
    def empty(self) -> bool:
        return self.size == 0

    def __len__(self) -> int:
        return self.size

    def clear(self) -> None:
        self._head = None
        self._tail = None
        self.size = 0
        self._iterator_node = None

    def __contains__(self, item: T) -> bool:
        current = self._head
        while current:
            if current.data == item:
                return True
            current = current.next
        return False

    def __iter__(self) -> ILinkedList[T]:
        self._iterator_node = self._head
        return self

    def __next__(self) -> T:
        if self._iterator_node is None:
            raise StopIteration
        data = self._iterator_node.data
        self._iterator_node = self._iterator_node.next
        return data
    
    def __reversed__(self) -> ILinkedList[T]:
        reversed_list = LinkedList(self._data_type)
        current = self._tail
        while current:
            reversed_list.append(current.data)
            current = current.previous
        return reversed_list
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, LinkedList):
            return False
        if self.size != other.size:
            return False

        node_self = self._head
        node_other = other._head

        while node_self and node_other:
            if node_self.data != node_other.data:
                return False
            node_self = node_self.next
            node_other = node_other.next

        return node_self is None and node_other is None


    def __str__(self) -> str:
        items = []
        current = self._head
        while current:
            items.append(repr(current.data))
            current = current.next
        return '[' + ', '.join(items) + ']'

    def __repr__(self) -> str:
        items = []
        current = self._head
        while current:
            items.append(repr(current.data))
            current = current.next
        return f"LinkedList({' <-> '.join(items)}) Count: {self.count}"


if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'OOPS!\nThis is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')
