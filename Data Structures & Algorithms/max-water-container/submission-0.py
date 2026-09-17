class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        ans = 0

        while l < r:
            length = r - l
            if ans < length * min(heights[l], heights[r]):
                ans = length * min(heights[l], heights[r])
            else: 
                if heights[l] < heights[r]:
                    l += 1
                else:
                    r -= 1
        return ans