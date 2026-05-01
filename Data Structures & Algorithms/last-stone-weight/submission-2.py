class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        mheap = [-stone for stone in stones]
        heapq.heapify(mheap)

        while len(mheap) > 1:
            x = -heapq.heappop(mheap)
            y = -heapq.heappop(mheap)
            z = x - y
            if z != 0: heapq.heappush(mheap, -z)


        return 0 if len(mheap) == 0 else -heapq.heappop(mheap)