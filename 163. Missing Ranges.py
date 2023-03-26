# Easy
# You are given an inclusive range [lower, upper] and a sorted unique integer array nums, 
# where all elements are in the inclusive range.
# A number x is considered missing if x is in the range [lower, upper] and x is not in nums.
# Return the smallest sorted list of ranges that cover every missing number exactly. 
# That is, 
# no element of nums is in any of the ranges, and each missing number is in one of the ranges.

# Each range [a,b] in the list should be output as:
# "a->b" if a != b
# "a" if a == b
 
# Example 1:
# Input: 
# nums = [0,1,3,50,75], 
# lower = 0, 
# upper = 99
# Output: 
# ["2","4->49","51->74","76->99"]

# Explanation: 
# The ranges are:
# [2,2] --> "2"
# [4,49] --> "4->49"
# [51,74] --> "51->74"
# [76,99] --> "76->99"

# Example 2:
# Input: 
# nums = [-1], 
# lower = -1,
# upper = -1
# Output: 
# []

# Explanation: 
# There are no missing ranges since there are no missing numbers.
 
# Constraints:
# -109 <= lower <= upper <= 109
# 0 <= nums.length <= 100
# lower <= nums[i] <= upper
# All the values of nums are unique.

# Solution
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        ans = []

        if nums == None or len(nums) == 0:
            if lower == upper:
                ans.append("{}".format(lower))
            elif lower < upper:
                ans.append("{}->{}".format(lower, upper))
            
            return ans

        if lower == nums[0] - 1:
            ans.append("{}".format(lower))
        elif lower < nums[0] - 1:
            ans.append("{}->{}".format(lower, nums[0] - 1))

        left = nums[0]

        for num in nums:
            if num == left + 2:
                ans.append("{}".format(left + 1))
            elif num > left + 2:
                ans.append("{}->{}".format(left + 1, num - 1))
            
            left = num
        
        if upper == nums[len(nums) - 1] + 1:
            ans.append("{}".format(upper))
        elif upper > nums[len(nums) - 1]:
            ans.append("{}->{}".format(nums[len(nums) - 1] + 1, upper))

        return ans
# TC: O(n); SC: O(1)
# Accepted



