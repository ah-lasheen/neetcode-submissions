class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}  # To store frequency of chars in the window
        max_count = 0  # Max frequency of any single char in window
        l = 0  # Left pointer
        max_len = 0  # Maximum length of valid substring

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1  # Add right char to frequency count
            max_count = max(max_count, freq[s[r]])  # Track the max occurring char

            # Check if we need to shrink the window
            while (r - l + 1) - max_count > k:
                freq[s[l]] -= 1  # Remove left char from window
                l += 1  # Move left pointer

            max_len = max(max_len, r - l + 1)  # Update max length

        return max_len