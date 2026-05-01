class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        res = 0
        new = []
        for num in nums:
            if num != val: 
                res += 1
                new.append(num)


        print(nums, new)

        for i in range(len(new)):
            nums[i] = new[i]

        return res
                