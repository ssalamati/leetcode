class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def recurse(i, cur):
            if i >= len(s):
                res.append(cur.copy())
                return

            for j in range(i + 1, len(s) + 1):
                if self.is_palindrome(s[i: j]):
                    cur.append(s[i: j])
                    recurse(j, cur)
                    cur.pop()

        recurse(0, [])

        return res

    def is_palindrome(self, s):
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return False

            l += 1
            r -= 1
        
        return True
