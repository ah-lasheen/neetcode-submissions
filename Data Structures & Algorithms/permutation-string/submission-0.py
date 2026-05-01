class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_chars = Counter(s1)
        window, window_count = len(s1), {}
        l, r = 0, 0

        while r < len(s2):
            window_count[s2[r]] = window_count.setdefault(s2[r], 0) + 1 
            if r - l + 1 > window:
                window_count[s2[l]] -= 1
                if window_count[s2[l]] == 0:
                    del window_count[s2[l]]
                l += 1

            if r - l + 1 == window and window_count == s1_chars:
                return True

            r += 1

        return window_count == s1_chars