class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            # m is our guessed eating speed
            # total is our hours spent eating at that speed
            m, total = (l + r) // 2, 0 

            for pile in piles:
                total += math.ceil(pile / m)

            if total <= h:
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        return res
