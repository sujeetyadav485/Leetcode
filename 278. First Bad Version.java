// Easy

// You are a product manager and currently leading a team to develop a new product. 
// Unfortunately, the latest version of your product fails the quality check. 
// Since each version is developed based on the previous version, all the versions after a bad version are also bad.

// Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

// You are given an API bool isBadVersion(version) which returns whether version is bad. 
// Implement a function to find the first bad version. You should minimize the number of calls to the API.

// Example 1:
// Input: n = 5, bad = 4
// Output: 4
// Explanation:
// call isBadVersion(3) -> false
// call isBadVersion(5) -> true
// call isBadVersion(4) -> true
// Then 4 is the first bad version.

// Example 2:
// Input: n = 1, bad = 1
// Output: 1
 
// Constraints:
// 1 <= bad <= n <= 231 - 1

/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

// Solution 1
public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        if (n <= 1) {
            return n;
        }
        
        int left = 0;
        int right = n;
        
        while (left < right - 1) {
            int mid = left + (right - left) / 2;
            
            if (isBadVersion(mid)) {
                right = mid;
            }
            else {
                left = mid;
            }
        }
        
        if (isBadVersion(left)) {
            return left;
        }
        else {
            return right;
        }       
    }
}
// TC: O(lgn): SC: O(1)

// Success
// Details 
// Runtime: 13 ms, faster than 42.08% of Java online submissions for First Bad Version.
// Memory Usage: 35.5 MB, less than 90.84% of Java online submissions for First Bad Version.

// Solution 2
public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        if (n == 1) {
            return n;
        }
             
        int left = 0;
        int right = n;
        
        while (left < right) {
            int mid = left + (right - left) / 2;
            
            if (isBadVersion(mid) == true) {
                right = mid;
            }
            else {
                left = mid + 1;
            }
        }
        
        return left;
    }
}
// TC: O(lgn); SC: O(1)

// Success
// Details 
// Runtime: 15 ms, faster than 30.12% of Java online submissions for First Bad Version.
// Memory Usage: 35.3 MB, less than 96.00% of Java online submissions for First Bad Version.
