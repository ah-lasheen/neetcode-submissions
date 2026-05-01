# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # first element of preorder is root
        # second element of preorder is the root of the first left subtree
        # everything to the left of find(preorder[0]) is in the left subtree
        # everything to the right (find(preorder[0]) + 1)

        if not preorder or not inorder: return None

        tree_root = TreeNode(preorder[0])       # The first node of the resulting tree
        midpoint = inorder.index(preorder[0])   # Get index of root in the inorder
        
        tree_root.left = self.buildTree(preorder[1:midpoint + 1], inorder[:midpoint])
        tree_root.right = self.buildTree(preorder[midpoint + 1:], inorder[midpoint + 1:])

        return tree_root