# Medium
# Given the head of a sorted linked list, 
# delete all nodes that have duplicate numbers, 
# leaving only distinct numbers from the original list. 
# Return the linked list sorted as well.

# Example 1:
# Input: head = [1,2,3,3,4,4,5]
# Output: [1,2,5]
  
# Example 2:
# Input: head = [1,1,1,2,3]
# Output: [2,3]
 
# Constraints:
# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.

# Solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        if head.next.next == None:
            if head.val == head.next.val:
                return None

            return head
        
        dummy = ListNode(0)
        dummy.next = head

        prv = dummy
        cur = prv.next
        nxt = cur.next
        cnt = 1
        
        while nxt:
            if nxt.val != cur.val:
                if cnt == 1:
                    prv.next = cur
                    prv = cur
                
                cur = nxt
                cnt = 1
            else:
                cnt += 1
            
            nxt = nxt.next
        
        if cnt == 1:
            prv.next = cur
            prv = cur
        
        prv.next = None

        return dummy.next
# TC: O(n); SC: O(1)
# Accepted
        
