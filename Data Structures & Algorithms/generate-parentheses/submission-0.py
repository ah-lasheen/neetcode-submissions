class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(curr, opened, closed):
            # n pairs of parenthesis means when we have a valid string of length 2 * n
            # we need to keep track of what is a valid parenthesis
            if len(curr) == n * 2:
                res.append("".join(curr))
                return
            if opened < n:
                curr.append("(")
                backtrack(curr, opened + 1, closed)
                curr.pop()
            if closed < opened:
                curr.append(")")
                backtrack(curr, opened, closed + 1)
                curr.pop()
            
            # if an empty curr, we need an opening parenthesis
            # if not an empty curr, we need to check the top of the stack
            # the stack can reach at max len == 3

        res = []
        backtrack([], 0, 0)
        return res