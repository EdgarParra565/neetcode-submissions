class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        minHeap = [[0, 0, 0]]
        visit = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while minHeap:
            diff, r, c = heapq.heappop(minHeap)
            if (r, c) in visit:
                continue
            visit.add((r, c))
            if (r, c) == (rows - 1, cols - 1):
                return diff
            for dr, dc in directions:
                newRow, newCol = r + dr, c + dc
                if (newRow < 0 or newCol < 0 or newRow == rows or newCol == cols or (newRow, newCol) in visit):
                    continue
                newDiff = max(abs(heights[r][c] - heights[newRow][newCol]), diff)
                heapq.heappush(minHeap, [newDiff, newRow, newCol])