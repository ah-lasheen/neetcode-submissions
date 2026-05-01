class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = Counter(nums)

        for k in freq.keys():
            if freq[k] > len(nums) / 2: return k

        return