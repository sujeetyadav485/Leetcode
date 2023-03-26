// Medium
// There are a total of numCourses courses you have to take, 
// labeled from 0 to numCourses - 1. 
// You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

// For example, 
// the pair [0, 1], 
// indicates that to take course 0 you have to first take course 1.
// Return the ordering of courses you should take to finish all courses. 
// If there are many valid answers, 
// return any of them. 
// If it is impossible to finish all courses, return an empty array.

// Example 1:
// Input: 
// numCourses = 2, 
// prerequisites = [[1,0]]
// Output: 
// [0,1]

// Explanation: 
// There are a total of 2 courses to take. 
// To take course 1 you should have finished course 0. 
// So the correct course order is [0,1].
  
// Example 2:
// Input: 
// numCourses = 4, 
// prerequisites = [[1,0],[2,0],[3,1],[3,2]]
// Output: 
// [0,2,1,3]

// Explanation: 
// There are a total of 4 courses to take. 
// To take course 3 you should have finished both courses 1 and 2. 
// Both courses 1 and 2 should be taken after you finished course 0.
// So one correct course order is [0,1,2,3]. 
// Another correct ordering is [0,2,1,3].
  
// Example 3:
// Input: 
// numCourses = 1, 
// prerequisites = []
// Output: 
// [0]

// Constraints:
// 1 <= numCourses <= 2000
// 0 <= prerequisites.length <= numCourses * (numCourses - 1)
// prerequisites[i].length == 2
// 0 <= ai, bi < numCourses
// ai != bi
// All the pairs [ai, bi] are distinct.
  
// Solution
class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        if (numCourses == 0 || prerequisites == null) {
            return new int[0];
        }
        
        int[] numPre = new int[numCourses];
        List<List<Integer>> preCrs = new ArrayList<>();
        
        for (int i = 0; i < numCourses; i++) {
            preCrs.add(new ArrayList<>());
        }
        
        for (int j = 0; j < prerequisites.length; j++) {
            preCrs.get(prerequisites[j][1]).add(prerequisites[j][0]);
            numPre[prerequisites[j][0]]++;
        }
        
        Queue<Integer> q = new ArrayDeque<>();
        
        for (int k = 0; k < numCourses; k++) {
            if (numPre[k] == 0) {
                q.offer(k);
            }
        }
        
        int[] ans = new int[numCourses];
        int cnt = 0;
        
        while (!q.isEmpty()) {
            int course = q.poll();
            
            ans[cnt] = course;
            cnt++;
            
            int len = preCrs.get(course).size();
            
            for (int l = 0; l < len; l++) {
                int afterCrs = preCrs.get(course).get(l);
                numPre[afterCrs]--;
                
                if (numPre[afterCrs] == 0) {
                    q.offer(afterCrs);
                }
            }   
        }
        
        return cnt == numCourses ? ans : new int[0]; 
    }
}
// TC: O(E + V); SC: O(E + V)
// Success
// Details 
// Runtime: 5 ms, faster than 90.12% of Java online submissions for Course Schedule II.
// Memory Usage: 48.4 MB, less than 55.51% of Java online submissions for Course Schedule II.
