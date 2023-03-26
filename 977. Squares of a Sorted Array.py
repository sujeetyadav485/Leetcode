# Easy
# Given an integer array nums sorted in non-decreasing order, 
# return an array of the squares of each number sorted in non-decreasing order.

# Example 1:
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
  
# Explanation: After squaring, 
# the array becomes [16,1,0,9,100].
# After sorting, 
# it becomes [0,1,9,16,100].

# Example 2:
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
 
# Constraints:
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in non-decreasing order.
 
# Follow up: 
# Squaring each element and sorting the new array is very trivial, 
# could you find an O(n) solution using a different approach?

# Solution 1
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []
        
        for n in nums:
            ans.append(n * n)
        
        ans.sort()
        
        return ans
# TC: O(nlgn); SC: O(1)
# Accepted

# Soluion 2
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)

        if nums[0] >= 0:
            for i in range(n):
                ans.append(nums[i] * nums[i])
        elif nums[n - 1] <= 0:
            for i in range(n - 1, -1, -1):
                ans.append(nums[i] * nums[i])
        else:
            left = 0
            right = 0

            for i in range(n - 1):
                if nums[i] * nums[i + 1] <= 0:
                    left = i
                    right = i + 1
            
            while left >= 0 and right < n:
                le_sq = nums[left] * nums[left]
                ri_sq = nums[right] * nums[right]

                if le_sq < ri_sq:
                    ans.append(le_sq)
                    left -= 1
                else:
                    ans.append(ri_sq)
                    right += 1
            
            while left >= 0:
                ans.append(nums[left] * nums[left])
                left -= 1
            
            while right < n:
                ans.append(nums[right] * nums[right])
                right += 1
        
        return ans
# TC: O(n); SC: O(1)
# Accepted

