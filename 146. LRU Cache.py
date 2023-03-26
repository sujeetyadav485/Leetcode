# Medium
# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

# Implement the LRUCache class:
# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, 
# otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. 
# Otherwise, add the key-value pair to the cache. 
# If the number of keys exceeds the capacity from this operation, 
# evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.

# Example 1:
# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]

# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4
 
# Constraints:
# 1 <= capacity <= 3000
# 0 <= key <= 104
# 0 <= value <= 105
# At most 2 * 105 calls will be made to get and put.

# Solution
class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        node = self.cache.get(key)

        if node:
            self.remove(node)
            self.append(node)

            return node.val
        
        return -1

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        
        if node:
            self.remove(node)
            node.val = value
        else:
            node = ListNode(key, value)
            size = len(self.cache)
        
            if size >= self.cap:
                remove_tail = self.tail
                self.remove(remove_tail)
        
        self.append(node)
        
    def remove(self, node):
        del self.cache[node.key]

        if node.prev:
            node.prev.next = node.next
        
        if node.next:
            node.next.prev = node.prev
        
        if node == self.head:
            self.head = self.head.next

        if node == self.tail:
            self.tail = self.tail.prev
        
        node.next = None
        node.prev = None
    
    def append(self, node):
        self.cache.setdefault(node.key, node)

        if self.head:
            node.next = self.head
            self.head.prev = node
        else:
            self.tail = node
        
        self.head = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# TC: O(1); SC: O(n)
# Accepted
