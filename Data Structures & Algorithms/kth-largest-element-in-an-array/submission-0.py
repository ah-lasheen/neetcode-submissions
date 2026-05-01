class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = []

        for num in nums: 
            heapq.heappush(res, num)
            print(res)
            if len(res) > k: heapq.heappop(res)

        return res[0]