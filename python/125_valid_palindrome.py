class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([ch for ch in s if ch.isalnum() or ch.isdigit()]).lower()

        r, l = 0, len(s) - 1

        while l >= r:
            if s[r] != s[l]:
                return False
            
            r += 1
            l -= 1

        return True
