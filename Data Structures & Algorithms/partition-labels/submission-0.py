class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndexApperance = {}

        for i, c in enumerate(s):
            lastIndexApperance[c] = i

        ans = []

        size = 0
        end = 0

        for i, c in enumerate(s):
            size += 1

            if lastIndexApperance[c] > end:
                end = lastIndexApperance[c]
            
            if i == end:
                ans.append(size)
                size = 0

        return ans