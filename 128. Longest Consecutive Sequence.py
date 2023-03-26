# Medium
# Given an unsorted array of integers nums, 
# return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

# Example 1:
# Input: 
# nums = [100,4,200,1,3,2]
# Output: 
# 4

# Explanation: 
# The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# Example 2:
# Input: 
# nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 
# 9
 
# Constraints:
# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109

# Solution
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        glb_max = 0
        cnt = 0
        cur = 0

        for num in num_set:
            if num - 1 not in num_set:
                cur = num
                cnt += 1
            
            while cur + 1 in num_set:
                cnt += 1
                cur += 1
            
            glb_max = max(glb_max, cnt)
            cnt = 0
        
        return glb_max
# TC: O(n); SC: O(n)
# Accepted
            

                


