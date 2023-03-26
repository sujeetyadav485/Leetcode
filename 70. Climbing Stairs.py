# Easy
# You are climbing a staircase. 
# It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. 
# In how many distinct ways can you climb to the top?

# Example 1:
# Input: 
# n = 2
# Output: 
# 2

# Explanation: 
# There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:
# Input: 
# n = 3
# Output: 
# 3

# Explanation: 
# There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
 
# Constraints:
# 1 <= n <= 45

# Solution 1
class Solution:
    def climbStairs(self, n: int) -> int:
        def helper(i, n):
            if i > n:
                return 0
            
            if i == n:
                return 1
            
            return helper(i + 1, n) + helper(i + 2, n)

        return helper(0, n)
# TC: O(2^n); SC: O(n)

# Solution 2
class Solution:
    def climbStairs(self, n: int) -> int:
        def helper(memo, i, n):
            if i > n:
                return 0
            
            if i == n:
                return 1
            
            if memo[i] > 0:
                return memo[i]
            
            memo[i] = helper(memo, i + 1, n) + helper(memo, i + 2, n)

            return memo[i]

        memo = [0] * (n + 1)

        return helper(memo, 0, n)
# TC: O(n); SC: O(n)
# Accepted
