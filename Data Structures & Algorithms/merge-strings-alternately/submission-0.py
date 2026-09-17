class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []
        minL = min(len(word1), len(word2))
        for i in range(minL):
            ans.append(word1[i])
            ans.append(word2[i])

        if len(word1) > len(word2):
            ans.append(word1[minL:])
        elif len(word2) > len(word1):
            ans.append(word2[minL:])
        return "".join(ans)