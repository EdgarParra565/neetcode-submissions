class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []

        l, r = 0, len(matrix[0])
        top, bot = 0, len(matrix) 
        
        while l < r and top < bot:
            for i in range(l, r):
                ans.append(matrix[top][i])
            top += 1
            
            for i in range(top, bot):
                ans.append(matrix[i][r - 1])
            r -= 1

            if not (l < r and top < bot):
                break
            
            for i in range(r - 1, l - 1, -1):
                ans.append(matrix[bot - 1][i])
            bot -= 1

            for i in range(bot - 1, top - 1, -1):
                ans.append(matrix[i][l])
            l += 1
        
        return ans