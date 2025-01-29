from typing import Iterable, Optional
from datastructures.ibag import IBag, T


class Bag(IBag[T]):
    def __init__(self, *items: Optional[Iterable[T]]) -> None:  #Need some help and the iterable initialization aspect of the bag.
        self.bag = {}
        self.bag_inventory = []


    def add(self, item: T) -> None:
        if item is not None:
            if item not in self.bag:
                self.bag[item] = 1
                self.bag_inventory.append(item)
            else:
                self.bag[item] += 1
        else:
            raise TypeError("Not a valid item")
        
    def remove(self, item: T) -> None:
        if item is not None:
            if item in self.bag:
                self.bag[item] -= 1
                if self.bag[item] == 0:
                    self.bag_inventory.remove(item)
                    del self.bag[item]
            else:
                raise ValueError(f"Item '{item}' not found in bag")
        else:
            raise TypeError("Not a valid item")

    def count(self, item: T) -> int:
        if item in self.bag:
            return self.bag[item]
        else:
            return 0
        

    def __len__(self) -> int:
      if len(self.bag_inventory) > 0:
          return sum(self.bag.values())     
      else:
          return 0

    def distinct_items(self) -> Iterable[T]:
        if len(self.bag_inventory) > 0:
            return self.bag_inventory
        else:
            raise TypeError("Bag is empty")
       

    def __contains__(self, item) -> bool:
        if item in self.bag_inventory:
            return True
        else:
            False

    def clear(self) -> None:
        if self.bag is not None:
            self.bag = {}
            self.bag_inventory = []
        else:
            return TypeError("Bag does not exist")