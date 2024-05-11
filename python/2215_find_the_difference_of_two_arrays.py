class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        set1, set2 = set(nums1), set(nums2)

        return [
            [n1 for n1 in set1 if n1 not in set2],
            [n2 for n2 in set2 if n2 not in set1],
        ]
