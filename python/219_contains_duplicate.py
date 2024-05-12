class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums_dict = {}

        for i, num in enumerate(nums):
            if num in nums_dict and i - nums_dict[num] <= k:
                return True
            nums_dict[num] = i
        
        return False
