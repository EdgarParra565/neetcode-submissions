class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        t = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]
        
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    t[i][j] = t[i - 1][j - 1] + 1
                else:
                    t[i][j] = max(t[i - 1][j], t[i][j - 1])
        return t[i][j]