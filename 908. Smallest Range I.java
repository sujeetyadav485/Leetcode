// Easy

// Given an array A of integers, for each integer A[i] we may choose any x with -K <= x <= K, and add x to A[i].

// After this process, we have some array B.

// Return the smallest possible difference between the maximum value of B and the minimum value of B.

// Example 1:

// Input: A = [1], K = 0
// Output: 0
// Explanation: B = [1]
// Example 2:

// Input: A = [0,10], K = 2
// Output: 6
// Explanation: B = [2,8]
// Example 3:

// Input: A = [1,3,6], K = 3
// Output: 0
// Explanation: B = [3,3,3] or B = [4,4,4]

// Note:

// 1 <= A.length <= 10000
// 0 <= A[i] <= 10000
// 0 <= K <= 10000

class Solution {
    public int smallestRangeI(int[] A, int K) {
        int min = A[0], max = A[0];
        
        for (int x: A) {
            min = Math.min(min, x);
            max = Math.max(max, x);
        }
        return Math.max(0, max - min - 2 * K);
    }
}

// Success
// Details 
// Runtime: 2 ms, faster than 82.07% of Java online submissions for Smallest Range I.
// Memory Usage: 40.1 MB, less than 39.16% of Java online submissions for Smallest Range I.
