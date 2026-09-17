class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                j, height = stack.pop()
                area = max(area, height * (i - j))
                start = j
            stack.append((start, h))

        for i, h in stack:
            area = max(area, h * (len(heights) - i))

        return area