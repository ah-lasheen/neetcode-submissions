# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # BST: Must always be true that (root.left.val < root.val < root.right.val)
        #      And that this is true down until the leaf nodes, leaf nodes are by def a BST

        def dfs(node, min_value, max_value):
            # If node is null from a leaf
            if not node: 
                return True

            # Comparing all nodes in the tree with the max and min values of each side
            if not (min_value < node.val < max_value):
                return False
            
            # recurse through the left side and then the right side, updating the boundary values
            return dfs(node.left, min_value, node.val) and dfs(node.right, node.val, max_value)

        return dfs(root, float('-inf'), float('inf'))