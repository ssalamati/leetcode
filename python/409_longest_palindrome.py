class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_set = set()

        res = 0
        for char in s:
            if char in char_set:
                res += 2
                char_set.remove(char)
            else:
                char_set.add(char)

        if char_set:
            res += 1

        return res
