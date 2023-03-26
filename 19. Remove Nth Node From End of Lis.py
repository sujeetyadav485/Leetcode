# Medium
# Given the head of a linked list, 
# remove the nth node from the end of the list and return its head.

# Example 1:
# Input: 
# head = [1,2,3,4,5], n = 2
# Output: 
# [1,2,3,5]

# Example 2:
# Input: 
# head = [1], n = 1
# Output: 
# []

# Example 3:
# Input: 
# head = [1,2], n = 1
# Output: 
# [1]
 
# Constraints:
# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz

# Follow up: 
# Could you do this in one pass?

# Solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        fast = dummy
        slow = dummy
        cnt = 0

        # while fast.next != None and cnt <= n:
        #     fast = fast.next
        #     cnt += 1
        for i in range(n + 1):
            fast = fast.next

        while fast != None:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next

        return dummy.next
# TC: O(n); SC: O(1)
# Accepted
