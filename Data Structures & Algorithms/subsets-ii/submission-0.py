class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        def backTrack(idx, comb):
            if idx == len(nums):
                ans.append(comb[::])
                return

            comb.append(nums[idx])
            backTrack(idx + 1, comb)
            comb.pop()
            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                idx += 1
            backTrack(idx + 1, comb)

        backTrack(0, [])

        return ans
