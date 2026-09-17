class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        r, c = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(row, col, visit, prev):
            if ((row, col) in visit or row < 0 or col < 0 or row == r or col == c or heights[row][col] < prev):
                return
            visit.add((row, col))
            dfs(row + 1, col, visit, heights[row][col])
            dfs(row - 1, col, visit, heights[row][col])
            dfs(row, col + 1, visit, heights[row][col])
            dfs(row, col - 1, visit, heights[row][col])

        for col in range(c):
            dfs(0, col, pac, heights[0][col])
            dfs(r - 1, col, atl, heights[r - 1][col])

        for row in range(r):
            dfs(row, 0, pac, heights[row][0])
            dfs(row, c - 1, atl, heights[row][c - 1])
        
        res = []
        for row in range(r):
            for col in range(c):
                if (row, col) in pac and (row, col) in atl:
                    res.append([row, col])

        return res