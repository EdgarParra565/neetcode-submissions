class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = {}

        def dfs(i, j, prev):
            if i == rows or i < 0 or j < 0 or j == cols or matrix[i][j] <= prev:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            
            res = 1
            res = max(
                res,
                1 + dfs(i + 1, j, matrix[i][j]), 
                1 + dfs(i - 1, j, matrix[i][j]),
                1 + dfs(i, j + 1, matrix[i][j]),
                1 + dfs(i, j - 1, matrix[i][j])
            )
            dp[(i, j)] = res

            return res
        
        m = -1
        for r in range(rows):
            for c in range(cols):
                m = max(m, dfs(r, c, -1))

        return m