class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        ans.append([])
        for i in nums:
            New = [subset + [i] for subset in ans]
            ans.extend(New)

        return ans