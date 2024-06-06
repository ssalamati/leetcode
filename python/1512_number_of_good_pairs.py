class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        visited = collections.defaultdict(int)
        res = 0

        for num in nums:
            if num in visited:
                res += visited[num]

            visited[num] += 1

        return res
