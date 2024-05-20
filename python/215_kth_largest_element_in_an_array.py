class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        left, right = 0, len(nums) - 1

        while left < right:
            pivot = self.partition(nums, left, right)

            if pivot < k:
                left = pivot + 1
            elif pivot > k:
                right = pivot - 1
            else:
                break

        return nums[k]

    def partition(self, nums, left, right) -> int:
        tmp = left

        for i in range(left, right):
            if nums[i] <= nums[right]:
                nums[i], nums[tmp] = nums[tmp], nums[i]
                tmp += 1

        nums[right], nums[tmp] = nums[tmp], nums[right]

        return tmp
