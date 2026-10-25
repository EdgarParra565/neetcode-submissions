class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        permutation = []
        count = {n:0 for n in nums}
        for n in nums:
            count[n] += 1
        
        def backtrack():
            if len(permutation) == len(nums):
                res.append(permutation.copy())
                return
            
            for n in count:
                if count[n] > 0:
                    permutation.append(n)
                    count[n] -= 1
                    backtrack()
                    count[n] += 1
                    permutation.pop()
        backtrack()
        return res