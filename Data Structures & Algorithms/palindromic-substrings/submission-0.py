class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def check(left, right):
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count

        total = 0

        for i in range(len(s)):
            total += check(i, i)
            total += check(i, i + 1)

        return total