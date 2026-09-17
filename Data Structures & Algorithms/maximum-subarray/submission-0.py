class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        cur = 0

        for a in nums:
            if cur < 0:
                cur = 0

            cur += a

            ans = max(ans, cur)
        
        return ans