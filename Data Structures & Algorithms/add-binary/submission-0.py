class Solution:
    def addBinary(self, a: str, b: str) -> str:
        AR = int(a,2)
        BR = int(b,2)
        ans = AR + BR
        return bin(ans)[2:]