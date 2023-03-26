# Easy
# Given an array nums of n integers where nums[i] is in the range [1, n], 
# return an array of all the integers in the range [1, n] that do not appear in nums.

# Example 1:
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]
  
# Example 2:
# Input: nums = [1,1]
# Output: [2]
 
# Constraints:
# n == nums.length
# 1 <= n <= 105
# 1 <= nums[i] <= n
 
# Follow up: 
# Could you do it without extra space and in O(n) runtime? 
# You may assume the returned list does not count as extra space.

# Solution
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        for i in range(n):
            cur = i
            
            while cur != nums[cur] - 1:
                if nums[cur] == -1:
                    nums[cur] = cur + 1
                    break
                else:
                    nxt = nums[cur] - 1
                    
                    if cur == i:
                        nums[cur] = -1
                    else:
                        nums[cur] = cur + 1

                    cur = nxt

        ans = []
        
        for j in range(n):
            if nums[j] - 1 != j:
                ans.append(j + 1)
        
        return ans
# TC: O(n); SC: O(1)
# Accepted
                
        
       
            
            
