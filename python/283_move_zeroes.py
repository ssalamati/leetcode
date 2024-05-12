class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        vacant = 0
        for num in nums:
            if num != 0:
                nums[vacant] = num
                vacant += 1

        while vacant < len(nums):
            nums[vacant] = 0
            vacant += 1
