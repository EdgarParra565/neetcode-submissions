class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = []
        while columnNumber > 0:
            columnNumber -= 1
            columnNumber, remainder = divmod(columnNumber, 26)

            ans.append(chr(remainder + 65)) 
        return "".join(ans[::-1])    