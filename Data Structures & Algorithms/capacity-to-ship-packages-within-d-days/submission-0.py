class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        while l <= r:
            m = (l + r) // 2
            reqDays = 1
            currW = 0
            for w in weights:
                if currW + w > m:
                    reqDays += 1
                    currW = 0              
                currW += w
            if reqDays <= days:
                r = m - 1           
            else:
                l = m + 1
        return l