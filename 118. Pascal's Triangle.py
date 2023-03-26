# Easy
# Given an integer numRows, 
# return the first numRows of Pascal's triangle.

# In Pascal's triangle, 
# each number is the sum of the two numbers directly above it as shown:

# Example 1:
# Input: 
# numRows = 5
# Output: 
# [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

# Example 2:
# Input: 
# numRows = 1
# Output: 
# [[1]]
 
# Constraints:
# 1 <= numRows <= 30

# Solution
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1], [1, 1]]

        if numRows == 1:
            return ans[0:1]
        
        if numRows == 2:
            return ans
        
        for i in range(3, numRows + 1):
            line = []

            for j in range(i):
                if j == 0 or j == i - 1:
                    line.append(1)
                else:
                    line.append(ans[i - 2][j - 1] + ans[i - 2][j])
            
            ans.append(line)

        return ans
# TC: O(n^2); SC: O(1)
# Accepted


