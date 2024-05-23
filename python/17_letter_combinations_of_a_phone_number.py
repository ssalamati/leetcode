class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return ""

        char_dict = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        res = []

        def dfs(i, cur):
            if i >= len(digits):
                res.append(cur.copy())
                return

            for char in char_dict[digits[i]]:
                cur.append(char)
                dfs(i + 1, cur)
                cur.pop()

        dfs(0, [])

        return ["".join(comb) for comb in res]
