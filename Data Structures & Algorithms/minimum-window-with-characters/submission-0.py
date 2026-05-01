class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""

        # added all chars in t to map with occurances & made copy
        ss_letters = Counter(t)
        ss_copy = ss_letters.copy()
        
        required_chars = len(t)
        result = ""
        min_len = float("inf")

        l, r = 0, 0
        # while chars of t still exist to search for in s
        while r < len(s):
            if ss_letters[s[r]] > 0:
                required_chars -= 1
            ss_letters[s[r]] -= 1
            
            while required_chars == 0:
                if (r - l + 1) < min_len:
                    min_len = r - l + 1
                    result = s[l:r + 1]

                if s[l] in ss_letters:
                    ss_letters[s[l]] += 1
                    if ss_letters[s[l]] > 0:
                        required_chars += 1

                l += 1
                
            r += 1
        return result
        