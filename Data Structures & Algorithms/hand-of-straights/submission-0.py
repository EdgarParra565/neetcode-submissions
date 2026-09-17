class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if not (len(hand) % groupSize == 0):
            return False

        hashmap = {}
        
        for h in hand:
            hashmap[h] = 1 + hashmap.get(h, 0)
        
        minH = list(hashmap.keys())
        heapq.heapify(minH)

        while minH:
            first = minH[0]
            
            for i in range(first, first + groupSize):
                if i not in hashmap:
                    return False
                hashmap[i] -= 1
                if hashmap[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        return True