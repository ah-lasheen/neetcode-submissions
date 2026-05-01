class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        res = []

        for i in range(k):
            key_max = max(freq, key=freq.get)
            res.append(key_max)
            del freq[key_max]

        res.reverse()
        return res