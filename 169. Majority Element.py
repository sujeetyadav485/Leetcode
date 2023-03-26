# Easy
# Given an array nums of size n, 
# return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. 
# You may assume that the majority element always exists in the array.

# Example 1:
# Input: 
# nums = [3,2,3]
# Output: 
# 3

# Example 2:
# Input: 
# nums = [2,2,1,1,1,2,2]
# Output: 
# 2
 
# Constraints:
# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109
 
# Follow-up: 
# Could you solve the problem in linear time and in O(1) space?

# Solution 1
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        slow = 0
        fast = 1

        while fast < n:
            while slow < fast and nums[slow] == 0:
                slow += 1

            if slow == fast:
                if fast == n - 1:
                    break
                else:
                    fast += 1

            if nums[fast] == nums[slow]:
                fast += 1
            else:
                nums[fast] = 0
                nums[slow] = 0
                fast += 1
        
        ans = 0
        i = 0

        while i < n:
            if nums[i] != 0:
                ans = nums[i]
                break
            i += 1
        
        return ans
# TC: O(n)； SC：O(1)
# Accepted

# Solution 2
class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
# TC: O(n): SC: O(1)
# Accepted

                
