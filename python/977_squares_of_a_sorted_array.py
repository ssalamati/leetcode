class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []

        neg = -1
        for i, num in enumerate(nums):
            if num < 0:
                neg = i
        pos = neg + 1

        while neg >= 0 and pos < len(nums):
            if (-1 * nums[neg]) > nums[pos]:
                res.append(nums[pos] ** 2)
                pos += 1
            else:
                res.append(nums[neg] ** 2)
                neg -= 1

        while neg >= 0:
            res.append(nums[neg] ** 2)
            neg -= 1

        while pos < len(nums):
            res.append(nums[pos] ** 2)
            pos += 1

        return res
