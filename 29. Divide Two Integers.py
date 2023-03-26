# Medium
# Given two integers dividend and divisor, 
# divide two integers without using multiplication, 
# division, 
# and mod operator.

# The integer division should truncate toward zero, 
# which means losing its fractional part. 
# For example, 
# 8.345 would be truncated to 8, 
# and -2.7335 would be truncated to -2.

# Return the quotient after dividing dividend by divisor.

# Note: 
# Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: 
# [−231, 231 − 1]. 
# For this problem, 
# if the quotient is strictly greater than 231 - 1, 
# then return 231 - 1, 
# and if the quotient is strictly less than -231, 
# then return -231.

# Example 1:
# Input: 
# dividend = 10, 
# divisor = 3
# Output: 
# 3

# Explanation: 
# 10/3 = 3.33333.. which is truncated to 3.

# Example 2:
# Input: 
# dividend = 7, 
# divisor = -3
# Output: 
# -2
# Explanation: 
# 7/-3 = -2.33333.. which is truncated to -2.

# Constraints:
# -231 <= dividend, divisor <= 231 - 1
# divisor != 0

# Solution 1
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        negtive = True
        upper = 2 ** 31 - 1
        lower = 2 ** 31

        if (dividend >= 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            negtive = False
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        cnt = 0

        while dividend >= divisor:
            dividend -= divisor
            cnt += 1

            if not negtive and cnt > upper:
                return upper

            if negtive and cnt > lower:
                return -lower
            
        if negtive:
            return -cnt
        
        return cnt
# TC: O(n); SC: O(1)
# Time Limit Exceeded

# Solution 2
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        negtive = True

        if (dividend >= 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            negtive = False
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        ans = 0
        power = 0
        upper = 2 ** 31 - 1
        lower = 2 ** 31

        while dividend >= divisor:
            temp = divisor
            power = 0

            while dividend >= temp:
                temp *= 2
                power += 1

            temp /= 2
            dividend -= temp
            temp = divisor
            power -= 1
            ans += 2 ** power

            if not negtive and ans > upper:
                return upper
            
            if negtive and ans > lower:
                return -lower
            
        if negtive:
            return -ans
        else:
            return ans
# TC: O(lgn); SC: O(1)
# Accepted
           
