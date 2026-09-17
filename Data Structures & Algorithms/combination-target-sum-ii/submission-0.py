class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()

        def backTrack(i, comb, total):
            if total == target:
                ans.append(comb[:])
                return

            if total > target or i >= len(candidates):
                return
            
            comb.append(candidates[i])
            backTrack(i + 1, comb, total + candidates[i])
            comb.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            
            backTrack(i + 1, comb, total)

        backTrack(0, [], 0)
        return ans
