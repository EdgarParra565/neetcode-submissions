class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(base, exp):
            ans = 1.0
            if exp == 0:
                return 1.0
            while exp > 0:
                if exp % 2 == 1:
                    ans *= base
                base *=base
                exp //= 2
            return ans

        if n >= 0:
            return helper(x,n)
        else:
            return 1.0 / helper(x, -n)
