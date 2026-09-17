class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)

        def backTrack(first):
            if first == n:
                ans.append(list(nums))
                return
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backTrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]

        backTrack(0)
        return ans