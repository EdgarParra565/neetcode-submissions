class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        ans1, ans2 = {}, {}

        for i in range(len(s)):
            ans1[s[i]] = 1 + ans1.get(s[i], 0)
            ans2[t[i]] = 1 + ans2.get(t[i], 0)
        return ans1 == ans2
