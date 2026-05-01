# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good = 0

        def dfs(max_val, node):
            if not node: return 0

            if node.val >= max_val:
                max_val = node.val
                self.good += 1

            if node.left:
                dfs(max_val, node.left)
            if node.right:
                dfs(max_val, node.right)

            return self.good

        return dfs(float("-inf"), root)

            