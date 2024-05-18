class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        chars = list(s)

        for i in range(len(s)):
            count += self.is_palindrome(chars, i, i)
            count += self.is_palindrome(chars, i, i + 1)

        return count

    def is_palindrome(self, chars: List[str], i: int, j: int) -> bool:
        count = 0

        while i >= 0 and j < len(chars) and chars[i] == chars[j]:
            count += 1
            i -= 1
            j += 1

        return count
