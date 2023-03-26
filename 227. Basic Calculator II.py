# Medium
# Given a string s which represents an expression, 
# evaluate this expression and return its value. 

# The integer division should truncate toward zero.

# You may assume that the given expression is always valid. 
# All intermediate results will be in the range of [-231, 231 - 1].

# Note: 
# You are not allowed to use any built-in function which evaluates strings as mathematical expressions, 
# such as eval().

# Example 1:
# Input: s = "3+2*2"
# Output: 7
  
# Example 2:
# Input: s = " 3/2 "
# Output: 1
  
# Example 3:
# Input: s = " 3+5 / 2 "
# Output: 5
 
# Constraints:
# 1 <= s.length <= 3 * 105
# s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
# s represents a valid expression.
# All the integers in the expression are non-negative integers in the range [0, 231 - 1].
# The answer is guaranteed to fit in a 32-bit integer.

# Solution
class Solution:
    def calculate(self, s: str) -> int:
        def update(num, sign):
            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-num)
            elif sign == '*':
                num = stack.pop(-1) * num
                stack.append(num)
            else:
                pre = stack.pop(-1)

                if pre >= 0:
                    num = pre // num
                    stack.append(num)
                else:
                    num = abs(pre) // num
                    stack.append(-num)
                
        stack = []
        i = 0
        num = 0
        sign = '+'

        while i < len(s):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            elif s[i] in '+-*/':
                update(num, sign)

                sign = s[i]
                num = 0

            i += 1

        update(num, sign)
        ans = sum(stack)

        return ans
# TC: O(n); SC:O(n)
# Accepted
