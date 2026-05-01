class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak, curr_streak = 0, 0
        seen = set(nums)

        for num in seen:
            if num - 1 not in seen:
                curr_num = num
                curr_streak = 1

                while curr_num + 1 in seen:
                    curr_num += 1
                    curr_streak += 1

            longest_streak = max(longest_streak, curr_streak)
        
        return longest_streak