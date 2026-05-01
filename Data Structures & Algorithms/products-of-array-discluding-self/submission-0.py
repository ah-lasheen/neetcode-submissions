class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
            ex: [1, 2, 4, 6] -> res = [48, 24, 12, 8]
        '''

        length = len(nums)
        left, right, res = [1] * length, [1] * length, [1] * length

        for i in range(1, length):
            left[i] = nums[i - 1] * left[i - 1]
        # given= [1, 2, 4, 6]
        # left = [1, 1, 2, 8]
        
        # expected right = [48, 24, 6, 1]
        for i in range(length - 2, -1, -1):
            right[i] = nums[i + 1] *  right[i + 1]
            res[i] = left[i] * right[i]

        length -= 1
        res[length] = left[length] * right[length]

        return res



