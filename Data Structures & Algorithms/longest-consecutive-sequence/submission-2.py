class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 1
        temp = 1
        if len(nums) == 0:
            return 0
        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            elif nums[i] - 1 == nums[i - 1]:
                temp += 1
                count = max(count, temp)
            else:
                temp = 1
        return count