# Medium
# Design your implementation of the linked list. 
# You can choose to use a singly or doubly linked list.
# A node in a singly linked list should have two attributes: 
# val and next. 
# val is the value of the current node, 
# and next is a pointer/reference to the next node.
# If you want to use the doubly linked list, 
# you will need one more attribute prev to indicate the previous node in the linked list. 
# Assume all nodes in the linked list are 0-indexed.

# Implement the MyLinkedList class:
# MyLinkedList() Initializes the MyLinkedList object.
# int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, 
# return -1.
# void addAtHead(int val) Add a node of value val before the first element of the linked list. 
# After the insertion, 
# the new node will be the first node of the linked list.
# void addAtTail(int val) Append a node of value val as the last element of the linked list.
# void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. 
# If index equals the length of the linked list,
# the node will be appended to the end of the linked list. 
# If index is greater than the length, 
# the node will not be inserted.
# void deleteAtIndex(int index) Delete the indexth node in the linked list, 
# if the index is valid.

# Example 1:
# Input
# ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
# [[], [1], [3], [1, 2], [1], [1], [1]]
# Output
# [null, null, null, null, 2, null, 3]

# Explanation
# MyLinkedList myLinkedList = new MyLinkedList();
# myLinkedList.addAtHead(1);
# myLinkedList.addAtTail(3);
# myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
# myLinkedList.get(1);              // return 2
# myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
# myLinkedList.get(1);              // return 3
 
# Constraints:
# 0 <= index, val <= 1000
# Please do not use the built-in LinkedList library.
# At most 2000 calls will be made to get, 
# addAtHead, 
# addAtTail, 
# addAtIndex and deleteAtIndex.

# Solution
class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        if index < self.size - 1 - index:
            cur = self.head.next
            cnt = 0

            while cnt < index:
                cur = cur.next
                cnt += 1
        else:
            cur = self.tail.prev
            cnt = self.size - 1 - index

            while cnt > 0:
                cur = cur.prev
                cnt -= 1
        
        return cur.val

    def addAtHead(self, val: int) -> None:
        nxt = self.head.next
        self.size += 1

        new_node = ListNode(val)

        new_node.prev = self.head
        self.head.next = new_node
        new_node.next = nxt
        nxt.prev = new_node

    def addAtTail(self, val: int) -> None:
        prv = self.tail.prev
        cur = self.tail
        self.size += 1

        new_node = ListNode(val)

        new_node.next = self.tail
        self.tail.prev = new_node
        new_node.prev = prv
        prv.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return

        if index < self.size - index:
            pred = self.head
            cnt = 0

            while cnt < index:
                pred = pred.next
                cnt += 1
            
            succ = pred.next
        else:
            succ = self.tail
            cnt = self.size - index

            while cnt > 0:
                succ = succ.prev
                cnt -= 1
            
            pred = succ.prev

        new_node = ListNode(val)
        new_node.prev = pred
        new_node.next = succ
        pred.next = new_node
        succ.prev = new_node

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        
        if index < self.size - 1 - index:
            cur = self.head.next
            cnt = 0

            while cnt < index:
                cur = cur.next
                cnt += 1
        else:
            cur = self.tail.prev
            cnt = self.size - 1 - index

            while cnt > 0:
                cur = cur.prev
                cnt -= 1
        
        cur.prev.next = cur.next
        cur.next.prev = cur.prev

        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# TC: O(1), O(n); SC: O(1)
# Accepted
