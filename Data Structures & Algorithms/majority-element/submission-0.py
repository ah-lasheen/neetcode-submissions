class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = Counter(nums)
        maximum = max(freq.values())
        for k, v in freq.items():
            if v == maximum: return k

        return