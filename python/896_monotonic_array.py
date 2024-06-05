class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing, decreasing = True, True

        for i in range(1, len(nums)):
            if not (nums[i] <= nums[i - 1]):
                decreasing = False

            if not (nums[i] >= nums[i - 1]):
                increasing = False

        return increasing or decreasing
