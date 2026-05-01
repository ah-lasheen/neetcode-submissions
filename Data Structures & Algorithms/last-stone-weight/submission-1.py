class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        mheap = [-x for x in stones]
        heapq.heapify(mheap)

        while len(mheap) > 1:
            first, second = -heapq.heappop(mheap), -heapq.heappop(mheap)
            if first - second != 0:
                heapq.heappush(mheap, -(first - second))

        return 0 if len(mheap) == 0 else -heapq.heappop(mheap)