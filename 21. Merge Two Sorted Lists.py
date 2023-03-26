# Easy
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list. 
# The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Example 1:
# Input: 
# list1 = [1,2,4], 
# list2 = [1,3,4]

# Output: 
# [1,1,2,3,4,4]

# Example 2:
# Input: 
# list1 = [], 
# list2 = []

# Output: 
# []

# Example 3:
# Input: 
# list1 = [], 
# list2 = [0]

# Output: 
# [0]
 
# Constraints:
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.

# Solution 1
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        cur1 = list1
        cur2 = list2

        while cur1 != None and cur2 != None:
            if cur1.val <= cur2.val:
                cur.next = cur1
                cur1 = cur1.next
            else:
                cur.next = cur2
                cur2 = cur2.next
            
            cur = cur.next

        while cur1 != None:
            cur.next = cur1
            cur = cur.next
            cur1 = cur1.next
        
        while cur2 != None:
            cur.next = cur2
            cur = cur.next
            cur2 = cur2.next
        
        return dummy.next
# TC: O(n); SC: O(1)
# Accepted

# Solution 2
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        
        if not list2:
            return list1

        l1 = list1
        l2 = list2
        dummy = ListNode(0)
        cur = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            
            cur = cur.next
            
        while l1:
            cur.next = l1
            l1 = l1.next
            cur = cur.next
        
        while l2:
            cur.next = l2
            l2 = l2.next
            cur = cur.next
        
        return dummy.next
# TC: O(n); SC: O(1)
# Accepted

# Solution 3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2
        dummy = ListNode(0)
        cur = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            
            cur = cur.next

        if l1:
            cur.next = l1
        
        if l2:
            cur.next = l2
        
        return dummy.next
# TC: O(n); SC: O(1)
# Accepted
