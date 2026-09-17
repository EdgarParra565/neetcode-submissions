class CountSquares:

    def __init__(self):
        self.ptsCount = defaultdict(int)
        self.pts = []

    def add(self, point):
        """
        :type point: List[int]
        :rtype: None
        """
        self.ptsCount[tuple(point)] += 1
        self.pts.append(point)

    def count(self, point):
        """
        :type point: List[int]
        :rtype: int
        """
        ans = 0

        px, py = point

        for x, y in self.pts:
            if (abs(py - y) != abs(px - x)) or x == px or y == py:
                continue
            ans += self.ptsCount[(x, py)] * self.ptsCount[(px, y)]
        return ans
