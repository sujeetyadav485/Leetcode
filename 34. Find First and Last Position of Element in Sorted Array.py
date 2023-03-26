# Medium
# Given an array of integers nums sorted in non-decreasing order, 
# find the starting and ending position of a given target value.
# If target is not found in the array, 
# return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: 
# nums = [5,7,7,8,8,10], target = 8
# Output: 
# [3,4]

# Example 2:
# Input: 
# nums = [5,7,7,8,8,10], target = 6
# Output: 
# [-1,-1]

# Example 3:
# Input: 
# nums = [], target = 0
# Output: 
# [-1,-1]
 
# Constraints:
# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109
# nums is a non-decreasing array.
# -109 <= target <= 109

# Solution
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)

        if size == 0:
            return [-1, -1]

        if size == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]

        left = 0
        right = size - 1
        find = False
        idx = 0

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                idx = mid
                find = True

                break
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
            
        if find:
            left = idx
            right = idx

            while left >= 0 and nums[left] == target:
                left -= 1
            
            while right < size and nums[right] == target:
                right += 1
            
            return [left + 1, right - 1]
        
        return [-1, -1]
# TC: O(lgn); SC: O(1)
# Accepted
        
