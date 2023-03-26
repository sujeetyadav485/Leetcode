# Medium
# Given a binary array nums, 
# return the maximum number of consecutive 1's in the array if you can flip at most one 0.

# Example 1:
# Input: nums = [1,0,1,1,0]
# Output: 4
  
# Explanation: 
# - If we flip the first zero, 
# nums becomes [1,1,1,1,0] and we have 4 consecutive ones.
# - If we flip the second zero, 
# nums becomes [1,0,1,1,1] and we have 3 consecutive ones.
# The max number of consecutive ones is 4.

# Example 2:
# Input: nums = [1,0,1,1,0,1]
# Output: 4
  
# Explanation: 
# - If we flip the first zero, 
# nums becomes [1,1,1,1,0,1] and we have 4 consecutive ones.
# - If we flip the second zero, 
# nums becomes [1,0,1,1,1,1] and we have 4 consecutive ones.
# The max number of consecutive ones is 4.
 
# Constraints:
# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.
 
# Follow up: 
# What if the input numbers come in one by one as an infinite stream? 
# In other words, 
# you can't store all numbers coming from the stream as it's too large to hold in memory. 
# Could you solve it efficiently?

# Solution
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        size = len(nums)

        before = 0
        after = 0
        glb_max = 0
        front = True
        
        for num in nums:
            if num == 0:
                if front:
                    front = False
                else:
                    glb_max = max(glb_max, before + after + 1)
                    before = after
                    after = 0
            else:
                if front:
                    before += 1
                else:
                    after += 1
        
        if front == True:
            return before

        glb_max = max(glb_max, before + after + 1)
        
        return glb_max
# TC: O(n); SC: O(1)                
# Accepted        
        
