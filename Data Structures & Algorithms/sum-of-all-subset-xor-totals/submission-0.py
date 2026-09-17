class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(i, total):
            if i == len(nums):
                return total

            notInclude = dfs(i + 1, total)
            include = dfs(i + 1, total ^ nums[i])

            return include + notInclude
        
        return dfs(0,0)        