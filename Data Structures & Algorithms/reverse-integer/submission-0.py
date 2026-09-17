class Solution:
    def reverse(self, x: int) -> int:
        s = abs(x)
        rs = 0
        while s:
            temp = s % 10
            s = s // 10
            if rs > math.pow(2, 31) // 10:
                return 0
                
            rs = rs * 10 + temp

        return rs if x > 0 else -rs