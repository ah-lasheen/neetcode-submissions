class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        freq = {}

        for n in nums:
            freq[n] = 1 + freq.get(n, 0)
        
        for key, val in freq.items():
            heapq.heappush(heap, (-val, key))

        res = []
        while len(res) < k:
            res.append(heapq.heappop(heap)[1])

        return res