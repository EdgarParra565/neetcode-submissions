class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minCount = float("inf")
        total = 0
        l = 0

        for r in range(len(nums)):
            total += nums[r]

            while total >= target:
                minCount = min(minCount, r - l + 1)
                total -= nums[l]
                l += 1

        if minCount == float("inf"):
            return 0
        return minCount