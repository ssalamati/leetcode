parantheses = {")": "(", "}": "{", "]": "["}

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for ch in s:
            if ch in parantheses.values():
                stack.append(ch)
            elif not stack or stack.pop() != parantheses[ch]:
                return False
        
        return not stack
