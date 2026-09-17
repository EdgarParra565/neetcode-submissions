class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        A, n = [1] + nums + [1], len(nums) + 2
        dp = [[0] * n for _ in range(n)]
        
        for left in range(n - 2, -1, -1):
            for right in range(left + 2, n):
                for last in range(left + 1, right):
                    coins = (
                        A[left] * A[last] * A[right]
                        + dp[left][last]
                        + dp[last][right]
                        )

                    dp[left][right] = max(dp[left][right], coins)

        return dp[0][n-1]