class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []

        def dfs(i, cur, total):
            if i >= len(candidates) and total == target:
                res.append(cur.copy())
                return

            if i >= len(candidates) or total > target:
                return

            cur.append(candidates[i])
            dfs(i + 1, cur, total + candidates[i])

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)

        return res
