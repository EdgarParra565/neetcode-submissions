class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        digitToChar = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"  
        }

        def backTrack(i, comb):
            if len(comb) == len(digits):
                ans.append(comb)
                return
            
            for j in digitToChar[digits[i]]:
                backTrack(i + 1, comb + j)

        if digits:
            backTrack(0, "")
        return ans