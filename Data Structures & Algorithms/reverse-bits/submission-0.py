class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0

        for i in range(32):
            ans = ans << 1
            bit = n % 2
            ans += bit
            n = n >> 1
        
        return ans