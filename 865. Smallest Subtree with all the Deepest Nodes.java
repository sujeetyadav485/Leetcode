// Medium
// Given the root of a binary tree, 
// the depth of each node is the shortest distance to the root.
// Return the smallest subtree such that it contains all the deepest nodes in the original tree.
// A node is called the deepest if it has the largest depth possible among any node in the entire tree.
// The subtree of a node is a tree consisting of that node, 
// plus the set of all descendants of that node.

// Example 1:
// Input: root = [3,5,1,6,2,0,8,null,null,7,4]
// Output: [2,7,4]

// Explanation: 
// We return the node with value 2, 
// colored in yellow in the diagram.
// The nodes coloured in blue are the deepest nodes of the tree.
// Notice that nodes 5, 3 and 2 contain the deepest nodes in the tree but node 2 is the smallest subtree among them, 
// so we return it.
  
// Example 2:
// Input: root = [1]
// Output: [1]

// Explanation: 
// The root is the deepest node in the tree.
  
// Example 3:
// Input: root = [0,1,3,null,2]
// Output: [2]

// Explanation: 
// The deepest node in the tree is 2, 
// the valid subtrees are the subtrees of nodes 2, 1 and 0 but the subtree of node 2 is the smallest.
 
// Constraints:
// The number of nodes in the tree will be in the range [1, 500].
// 0 <= Node.val <= 500
// The values of the nodes in the tree are unique.
 
// Note: This question is the same as 1123: https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/

// Solution
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode subtreeWithAllDeepest(TreeNode root) {
        if (root == null) {
            return root;
        }
        
        int[] maxDepth = new int[] {0};
        int[] depth = new int[] {0};
        List<TreeNode> deepestNodes = new ArrayList<>();
        
        findDeepestNodes(root, maxDepth, depth, deepestNodes);
        Set<TreeNode> dNSet = buildSet(deepestNodes);
        TreeNode ans = lowestCommonAncestor(root, dNSet);
        
        return ans;
    }
    
    private void findDeepestNodes(TreeNode root, int[] maxDepth, int[] depth, List<TreeNode> deepestNodes) {
        depth[0]++;
        
        if (root.left == null && root.right == null) {
            if (depth[0] > maxDepth[0]) {
                maxDepth[0] = depth[0];
                deepestNodes.clear();
                deepestNodes.add(root);
            }
            else if (depth[0] == maxDepth[0]) {
                deepestNodes.add(root);
            }
            
            return;
        }
        
        if (root.left != null) {
            findDeepestNodes(root.left, maxDepth, depth, deepestNodes);
            depth[0]--;
        }
        
        if (root.right != null) {
            findDeepestNodes(root.right, maxDepth, depth, deepestNodes);
            depth[0]--;
        }
    }
    
    private TreeNode lowestCommonAncestor(TreeNode root, Set<TreeNode> dNSet) {
        if (root == null) {
            return null;
        }
        
        if (dNSet.contains(root)) {
            return root;
        }
        
        TreeNode leftChild = lowestCommonAncestor(root.left, dNSet);
        TreeNode rightChild = lowestCommonAncestor(root.right, dNSet);
        
        if (leftChild != null && rightChild != null) {
            return root;
        }
        
        return leftChild == null ? rightChild : leftChild;
    }
    
    private Set<TreeNode> buildSet(List<TreeNode> deepestNodes) {
        Set<TreeNode> dNSet = new HashSet<>();
        
        for (TreeNode node : deepestNodes) {
            dNSet.add(node);
        }
        
        return dNSet;
    }
}
// TC: O(n); SC: O(height)
// Success
// Details 
// Runtime: 2 ms, faster than 21.55% of Java online submissions for Smallest Subtree with all the Deepest Nodes.
// Memory Usage: 42.4 MB, less than 31.29% of Java online submissions for Smallest Subtree with all the Deepest Nodes.
