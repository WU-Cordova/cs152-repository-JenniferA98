import copy
from typing import Callable, Iterator, Optional, Tuple
from datastructures.ihashmap import KT, VT, IHashMap
from datastructures.array import Array
import pickle
import hashlib

from datastructures.linkedlist import LinkedList

class HashMap(IHashMap[KT, VT]):

    def __init__(self, number_of_buckets=7, load_factor=0.75, data_type: type = object, custom_hash_function: Optional[Callable[[KT], int]]=None) -> None:
        self._buckets: Array[ LinkedList[Tuple[KT, VT]]] = [LinkedList() for buckets in range(number_of_buckets)]
        self._count = 0
        self._load_factor = load_factor
        self.data_type = data_type
        self._hash_function = custom_hash_function if custom_hash_function else self._default_hash_function

    def __getitem__(self, key: KT) -> VT:
        index = self._get_bucket_index(key)
        bucket = self._buckets[index]
        for k, v in bucket:
            if k== key:
                return v
        raise KeyError(f"Key {key} not found.")

    def __setitem__(self, key: KT, value: VT) -> None:        
        if not isinstance(value, self.data_type):
            raise TypeError(f"Expected value of type {self.data_type.__name__}")

        index = self._get_bucket_index(key)

        if not 0 <= index < len(self._buckets):
            raise IndexError(f"Bucket index {index} out of range.")
        
        bucket = self._buckets[index]

        for node in bucket:
            if node[0] == key:
                node[1] = value
                return

        bucket.append([key, value])
        self._count += 1

        if self._count / len(self._buckets) > self._load_factor:
            self._rehash()
    

    def keys(self) -> Iterator[KT]:
        for k, in self.items():
            yield k

    def _get_bucket_index(self, key:KT) -> int:
        return self._hash_function(key) % len(self._buckets)
    
    def values(self) -> Iterator[VT]:
        for _, v in self.items():
            yield v

    def items(self) -> Iterator[Tuple[KT, VT]]:
        for bucket in self._buckets:
            for item in bucket:
                yield item
            
    def __delitem__(self, key: KT) -> None:
        index = self._get_bucket_index(key)
        bucket = self._buckets[index]

        for item in bucket:
            if item[0] == key:
                bucket.remove(item)
                self._count -=2
                return
            
        raise KeyError(f"Key {key} not found.")
                
    
    def __contains__(self, key: KT) -> bool:
        index = self._get_bucket_index(key)
        bucket = self._buckets[index]

        for k, _ in bucket:
            if k == key:
                return True
        return False
    
    def __len__(self) -> int:
        return self._count
    
    def __iter__(self) -> Iterator[KT]:
        for bucket in self._buckets:
            for k, _ in bucket:
                yield k
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, HashMap):
            return False
        if len(self) != len(other):
            return False
        for k, v in self.items():
            if k not in other or other[k] != v:
                return False
        return True

    def __str__(self) -> str:
        return "{" + ", ".join(f"{k}: {v}" for k, v in self.items()) + "}"
    
    def __repr__(self) -> str:
        return f"HashMap({str(self)})"
    
    def _rehash(self):
        prev_items = list(self.items())
        new_capacity = HashMap._next_prime(len(self._buckets) * 2)
        self._buckets = [LinkedList() for _ in range(new_capacity)]
        self._count = 0

        for key, value in prev_items:
            self[key] = value


    @staticmethod
    def _default_hash_function(key: KT) -> int:
        """
        Default hash function for the HashMap.
        Uses Pickle to serialize the key and then hashes it using SHA-256. 
        Uses pickle for serialization (to capture full object structure).
        Falls back to repr() if the object is not pickleable (e.g., open file handles, certain C extensions).
        Returns a consistent integer hash.
        Warning: This method is not suitable
        for keys that are not hashable or have mutable state.

        Args:
            key (KT): The key to hash.
        Returns:
            int: The hash value of the key.
        """
        try:
            key_bytes = pickle.dumps(key)
        except Exception:
            key_bytes = repr(key).encode()
        return int(hashlib.md5(key_bytes).hexdigest(), 16)
    
    @staticmethod
    def _is_prime(n:int) -> bool:
        if (n < 2) or (n % 2 == 0):
            return False
        if n == 2:
            return True
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    
    @staticmethod
    def _next_prime(n: int) -> int:
        if HashMap._is_prime(n):
            return n
        return HashMap._next_prime(n+1)
        