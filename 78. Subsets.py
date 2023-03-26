# Medium
# Given an integer array nums of unique elements, 
# return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. 
# Return the solution in any order.

# Example 1:
# Input: 
# nums = [1,2,3]
# Output: 
# [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

# Example 2:
# Input: 
# nums = [0]
# Output: 
# [[],[0]] 

# Constraints:
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.

# Solution
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        rslt = []
        ans = []
        
        self.dfs(nums, ans, rslt, 0, len(nums))

        return ans
    
    def dfs(self, nums, ans, rslt, idx, n):
        if idx == n:
            l = copy.deepcopy(rslt)
            ans.append(l)

            return

        digit = nums[idx]

        rslt.append(digit)
        self.dfs(nums, ans, rslt, idx + 1, n)
        rslt.pop()
        self.dfs(nums, ans, rslt, idx + 1, n)
# TC: O(2^n); SC: O(n)
# Accepted




        
        
