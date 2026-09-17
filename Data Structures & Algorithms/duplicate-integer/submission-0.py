class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ans = set(nums)
        if len(ans) == len(nums):
            return False
        else: 
            return True