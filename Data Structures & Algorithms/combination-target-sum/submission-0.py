class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        def backTrack(idx, comb, total):
            if total == target:
                ans.append(comb[:])
                return
            if total > target or idx >= len(nums):
                return
            comb.append(nums[idx])
            backTrack(idx, comb, total + nums[idx])
            comb.pop()
            backTrack(idx + 1, comb, total)
            return ans

        return backTrack(0, [], 0)