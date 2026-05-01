class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def depth(node: Optional[TreeNode]) -> int:
            if not node: return -1

            nonlocal diameter

            left_path = depth(node.left)
            right_path = depth(node.right)

            diameter = max(diameter, left_path + right_path + 2)

            return 1 + max(left_path, right_path)

        depth(root)
        return diameter
