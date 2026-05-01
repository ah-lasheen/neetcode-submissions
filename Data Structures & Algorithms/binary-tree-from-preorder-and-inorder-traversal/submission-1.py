# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # first element of preorder is root
        # everything to the left of find(preorder[0]) is in the left subtree
        # everything to the right (find(preorder[0]) + 1)

        if not preorder or not inorder: return None

        tree_root = TreeNode(preorder[0])       # The first node of the resulting tree
        midpoint = inorder.index(preorder[0])   # Get index of root in the inorder
        
        # left subtree built from:
        #   - preorder[1:midpoint + 1] (elements after root up to the midpoint)
        #   - inorder[:midpoint] (elements before the midpoint in inorder)
        tree_root.left = self.buildTree(preorder[1:midpoint + 1], inorder[:midpoint])

        # right subtree built from:
        #   - preorder[midpoint + 1:] (elements after the left subtree in preorder)
        #   - inorder[midpoint + 1:] (elements after the midpoint in inorder)
        #
        #   Ex: Given preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
        #     tree_root = 3
        #     left_subtree = [9] (from inorder[:midpoint])
        #     right_subtree = [15, 20, 7] (from inorder[midpoint + 1:])
        #     The preorder for the right subtree starts after the left subtree elements: -> preorder[midpoint + 1:] 
        tree_root.right = self.buildTree(preorder[midpoint + 1:], inorder[midpoint + 1:])

        return tree_root