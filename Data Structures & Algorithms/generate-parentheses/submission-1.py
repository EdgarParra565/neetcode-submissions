class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backTrack(path, openCount, closeCount):
            if len(path) == 2 * n:
                ans.append(path)
                return
            
            if openCount < n:
                backTrack(path + "(", openCount + 1, closeCount)
            if closeCount < openCount:
                backTrack(path + ")", openCount, closeCount + 1)


        backTrack("", 0 , 0)
        return ans
