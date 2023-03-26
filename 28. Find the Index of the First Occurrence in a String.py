# Medium
# Given two strings needle and haystack, 
# return the index of the first occurrence of needle in haystack, 
# or -1 if needle is not part of haystack.

# Example 1:
# Input: 
# haystack = "sadbutsad", 
# needle = "sad"
# Output: 0
  
# Explanation: 
# "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, 
# so we return 0.

# Example 2:
# Input: 
# haystack = "leetcode", 
# needle = "leeto"
# Output: 
# -1

# Explanation: 
# "leeto" did not occur in "leetcode", 
# so we return -1.
 
# Constraints:
# 1 <= haystack.length, 
# needle.length <= 104
# haystack and needle consist of only lowercase English characters.

# Solution
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_needle = len(needle)
        len_haystack = len(haystack)
        
        for i in range(len_haystack):
            j = 0
            k = i

            while k < len_haystack and haystack[k] == needle[j]:
                k += 1
                j += 1

                if j == len_needle:
                    return i
        
        return -1
# TC: O(n*m); SC: O(1)
# Accepted

