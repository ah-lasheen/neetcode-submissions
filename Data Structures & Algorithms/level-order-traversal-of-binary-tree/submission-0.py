# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        q, res = deque([root]), []

        while q:
            q_len = len(q)
            level = []

            for i in range(q_len):
                parent = q.popleft()
                if parent: # children of nodes can be null, so dont add these nodes' children to level
                    level.append(parent.val)
                    q.append(parent.left)
                    q.append(parent.right)
            if level:
                res.append(level)

        return res

        
