class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l <= r:
            m = (l + r) // 2
            if x > m ** 2:
                l = m + 1
            elif x < m ** 2:
                r = m - 1
            else:
                return m
        return r
