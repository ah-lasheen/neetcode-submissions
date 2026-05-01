# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # bfs: make final list of last elements in each level
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([root])
        right_side = []

        while q:
            length, level = len(q), []
            for i in range(length):
                curr = q.popleft()
                if curr:
                    level.append(curr.val)
                    q.append(curr.left)
                    q.append(curr.right)
            if level:
                right_side.append(level[-1])

        return right_side