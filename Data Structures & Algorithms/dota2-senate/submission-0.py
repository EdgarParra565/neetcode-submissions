class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        DQueue, RQueue = deque(), deque()

        for i, c in enumerate(senate):
            if c == "R":
                RQueue.append(i)
            else:
                DQueue.append(i)

        while DQueue and RQueue:
            dTurn = DQueue.popleft()
            rTurn = RQueue.popleft()

            if rTurn < dTurn:
                RQueue.append(dTurn + len(senate))
            else:
                DQueue.append(rTurn + len(senate))

        return "Radiant" if RQueue else "Dire"
        