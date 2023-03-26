// Medium
// Given n non-negative integers a1, a2, ..., an , 
// where each represents a point at coordinate (i, ai). 
// n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
// Find two lines, which together with x-axis forms a container, 
// such that the container contains the most water.

// Note: 
// You may not slant the container and n is at least 2.

// Example:
// Input: [1,8,6,2,5,4,8,3,7]
// Output: 49

// Solution 1
class Solution {
    public int maxArea(int[] height) {
        int area = 0, i = 0, j = height.length - 1;
        
        while (i < j) {
            int temp = Math.min(height[i], height[j]) * (j - i);
            area = Math.max(area, temp);
            
            if (height[i] > height[j]) {
                j--;
            }
            else {
                i++;
            }
        }
        return area;
    }
}
// Success
// Details 
// Runtime: 6 ms, faster than 30.94% of Java online submissions for Container With Most Water.
// Memory Usage: 45.9 MB, less than 5.26% of Java online submissions for Container With Most Water.

// Solution 2
class Solution {
    public int maxArea(int[] height) {
        int left = 0;
        int right = height.length - 1;
        int glbMax = 0;
        
        while (left < right) {
            int minBar = Math.min(height[left], height[right]);
            int area = minBar * (right - left);
            
            glbMax = Math.max(glbMax, area);
            
            if (height[left] < height[right]) {
                left++;
            }
            else if (height[left] > height[right]) {
                right--;
            }
            else {
                left++;
                right--;
            }
        }
        
        return glbMax;
    }
}
// TC: O(n); SC: O(1)
// Success
// Details 
// Runtime: 4 ms, faster than 84.27% of Java online submissions for Container With Most Water.
// Memory Usage: 52.7 MB, less than 91.19% of Java online submissions for Container With Most Water.
