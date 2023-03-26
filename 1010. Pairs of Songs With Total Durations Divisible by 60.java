// Medium
// You are given a list of songs where the ith song has a duration of time[i] seconds.
// Return the number of pairs of songs for which their total duration in seconds is divisible by 60. 
// Formally, 
// we want the number of indices i, 
// j such that i < j with (time[i] + time[j]) % 60 == 0.

// Example 1:
// Input: time = [30,20,150,100,40]
// Output: 3
  
// Explanation: 
// Three pairs have a total duration divisible by 60:
// (time[0] = 30, time[2] = 150): total duration 180
// (time[1] = 20, time[3] = 100): total duration 120
// (time[1] = 20, time[4] = 40): total duration 60
  
// Example 2:
// Input: time = [60,60,60]
// Output: 3
  
// Explanation: 
// All three pairs have a total duration of 120, which is divisible by 60.
 
// Constraints:
// 1 <= time.length <= 6 * 104
// 1 <= time[i] <= 500
  
// Solution
class Solution {
    public int numPairsDivisibleBy60(int[] time) {
        int[] complement = new int[60];
        int ans = 0;
        
        for (int t : time) {
            if (t % 60 == 0) {
                ans += complement[0];
            }
            else {
                ans += complement[60 - t % 60];
            }
            
            complement[t % 60]++;
        }
        
        return ans;
    }
}
// TC: O(n); SC: O(1)
// Success
// Details 
// Runtime: 4 ms, faster than 79.34% of Java online submissions for Pairs of Songs With Total Durations Divisible by 60.
// Memory Usage: 54.2 MB, less than 55.58% of Java online submissions for Pairs of Songs With Total Durations Divisible by 60.
