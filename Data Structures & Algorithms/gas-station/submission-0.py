class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        amount = 0
        ans = 0

        for i in range(len(gas)):
            amount += (gas[i] - cost[i])

            if amount < 0:
                amount = 0
                ans = i + 1
        
        return ans