# Medium
# Given a string s, 
# partition s such that every substring of the partition is a palindrome. 
# Return all possible palindrome partitioning of s.

# Example 1:
# Input: 
# s = "aab"
# Output: 
# [["a","a","b"],["aa","b"]]

# Example 2:
# Input: 
# s = "a"
# Output: 
# [["a"]]
 
# Constraints:
# 1 <= s.length <= 16
# s contains only lowercase English letters.

# Solution
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        cnstrct = []
        n = len(s)

        self.dfs(s, 0, ans, cnstrct, n)

        return ans
    
    def dfs(self, s, start, ans, cnstrct, n):
        if start == n:
            ans.append(copy.deepcopy(cnstrct))

            return

        for end in range(start, n):
            if self.isPalindrome(s, start, end):
                cnstrct.append(s[start:end + 1]) 
                self.dfs(s, end + 1, ans, cnstrct, n)
                cnstrct.pop(-1)
    
    def isPalindrome(self, s, start, end):
        while start < end:
            if s[start] != s[end]:
                return False
            
            start += 1
            end -= 1
        
        return True
# TC: O(n * 2 ^ n); SC: O(n)
# Accepted

        
