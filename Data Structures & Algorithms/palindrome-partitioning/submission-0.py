class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        part = []

        def isPalindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left, right = left + 1, right - 1
            return True

        def backTrack(idx):
            if idx >= len(s):
                ans.append(part[:])
                return
            for j in range(idx, len(s)):
                if isPalindrome(idx, j):
                    part.append(s[idx : j + 1])
                    backTrack(j + 1)
                    part.pop()
            
        backTrack(0)
        return ans