class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        leftM = rightM = 0
        total = 0

        if len(height) < 3:
            return 0
        
        while l < r:
            if height[l] < height[r]:
                if height[l] >= leftM:
                    leftM = height[l] 
                else:
                    total += leftM - height[l]
                l += 1
            else:
                if height[r] >= rightM:
                    rightM = height[r]
                else:
                    total += rightM - height[r]
                r -= 1
        return total