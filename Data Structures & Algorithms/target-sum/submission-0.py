class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)

        dp[0] = 1

        for i in range(len(nums)):
            nextdp = defaultdict(int)
            for cur, count in dp.items():
                nextdp[cur + nums[i]] += count
                nextdp[cur - nums[i]] += count
            dp = nextdp
    
        return dp[target] 