class Solution:
    def hammingWeight(self, n: int) -> int:
        
        stringN = bin(n)
        count = 0

        for c in stringN:
            if c == "1":
                count += 1

        return count