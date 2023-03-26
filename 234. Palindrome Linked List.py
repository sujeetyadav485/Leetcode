# Easy
# Given the head of a singly linked list, 
# return true if it is a palindrome or false otherwise.

# Example 1:
# Input: 
# head = [1,2,2,1]
# Output: 
# true
  
# Example 2:
# Input: 
# head = [1,2]
# Output: 
# false
 
# Constraints:
# The number of nodes in the list is in the range [1, 105].
# 0 <= Node.val <= 9
 
# Follow up: 
# Could you do it in O(n) time and O(1) space?

# Solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None:
            return True

        first_end = self.find_mid(head)
        second_start = first_end.next
        second_cur = self.reverse(second_start)
        first_cur = head

        while first_cur != second_cur and second_cur != None:
            if first_cur.val != second_cur.val:
                return False

            first_cur = first_cur.next
            second_cur = second_cur.next

        return True 

    def find_mid(self, head):
        fast = head
        slow = head

        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next

        return slow

    def reverse(self, head):
        prv = None
        cur = head

        while cur != None:
            nxt = cur.next
            cur.next = prv
            prv = cur
            cur = nxt

        return prv
# TC: O(n); SC: O(1)
# Accepted
