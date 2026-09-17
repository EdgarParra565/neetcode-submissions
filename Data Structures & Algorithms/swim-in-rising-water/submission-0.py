class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visit = set()
        minHeap = [[grid[0][0], 0, 0]]
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        visit.add((0,0))

        while minHeap:
            t, r, c = heapq.heappop(minHeap)

            if r == n -1 and c == n - 1:
                return t
            
            for dr, dc in directions:
                neighborR, neighborC = r + dr, c + dc
                if (neighborR < 0 or neighborC < 0 or neighborR == n or neighborC == n) or ((neighborR, neighborC) in visit):
                    continue
                visit.add((neighborR, neighborC))

                newTime = max(t, grid[neighborR][neighborC])

                heapq.heappush(minHeap, (newTime, neighborR, neighborC))      