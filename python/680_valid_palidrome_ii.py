class Solution:
    def validPalindrome(self, s: str) -> bool:
        return self.is_palindrome(s, 0, len(s) - 1, False)
    
    def is_palindrome(self, s, l, r, d) -> bool:
        if l > r:
            return True

        if s[l] == s[r]:
            return self.is_palindrome(s, l + 1, r - 1, d)
        elif d:
            return False
        
        return self.is_palindrome(s, l + 1, r, True) or self.is_palindrome(s, l, r - 1, True)
