class Solution:
    def canJump(self, nums: List[int]) -> bool:
        point = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= point:
                point = i
        
        if point == 0:
            return True
        else:
            return False
        