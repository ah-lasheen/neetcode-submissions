# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        if both p and q are less than the root, we know both are in the left subtree
        same thing with both greater than root
        depending on this, recurse down the tree where both nodes are
        when we get to a subtree where p and q are in different trees, we know we have the LCA
        '''
        
        if not root: return None

        if root.val == p.val or root.val == q.val or (p.val < root.val and root.val < q.val) or (q.val < root.val and root.val < p.val):
            return root
    
        if p.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else: 
            return self.lowestCommonAncestor(root.right, p, q)
