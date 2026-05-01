class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ans, l, r = 0, 1, max(piles)

        while l <= r:
            m = (l + r) // 2
            hours = sum((pile + m - 1) // m for pile in piles)

            print(hours)

            if hours <= h:
                ans = m
                r = m - 1
            else: 
                l = m + 1

        return ans