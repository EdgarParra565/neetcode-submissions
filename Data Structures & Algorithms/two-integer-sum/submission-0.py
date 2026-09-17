class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = {}

        for i in range(len(nums)):
            lookup = target - nums[i]
            if lookup in ans:
                return [ans[lookup], i]    
            ans[nums[i]] = i
            
        