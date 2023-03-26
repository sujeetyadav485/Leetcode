// Medium
// Given an array of distinct integers candidates and a target integer target, 
// return a list of all unique combinations of candidates where the chosen numbers sum to target. 
// You may return the combinations in any order.

// The same number may be chosen from candidates an unlimited number of times. 
// Two combinations are unique if the frequency of at least one of the chosen numbers is different.

// It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

// Example 1:
// Input: candidates = [2,3,6,7], target = 7
// Output: [[2,2,3],[7]]

// Explanation:
// 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
// 7 is a candidate, and 7 = 7.
// These are the only two combinations.
  
// Example 2:
// Input: candidates = [2,3,5], target = 8
// Output: [[2,2,2,2],[2,3,3],[3,5]]

// Example 3:
// Input: candidates = [2], target = 1
// Output: []
 
// Constraints:
// 1 <= candidates.length <= 30
// 1 <= candidates[i] <= 200
// All elements of candidates are distinct.
// 1 <= target <= 500
  
// Solution
class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        if (candidates == null || candidates.length == 0) {
            return null;
        }
        
        List<List<Integer>> ans = new ArrayList<>();
        List<Integer> temp = new ArrayList<>();
    
        helperDFS(candidates, target, 0, 0, temp, ans);
        
        return ans;
    }
    
    private void helperDFS(int[] candi, int target, int sum, int index, List<Integer> temp, List<List<Integer>> ans) {
        if (sum >= target) {
            if (sum == target) {
                List<Integer> tempAdd = new ArrayList<>(temp);
                ans.add(tempAdd);
            }
            
            return;
        }
        
        for (int i = index; i < candi.length; i++) {
            sum += candi[i];
            temp.add(candi[i]);
            
            helperDFS(candi, target, sum, i, temp, ans);
            
            sum -= candi[i];
            temp.remove(temp.size() - 1);
        }
    }
}
// TC: O(n^(t/m + 1); SC: O(t/m)
// Let n be the number of candidates, 
// t be the target value, 
// and m be the minimal value among the candidates.
// Success
// Details 
// Runtime: 9 ms, faster than 30.07% of Java online submissions for Combination Sum.
// Memory Usage: 44.6 MB, less than 37.45% of Java online submissions for Combination Sum.
