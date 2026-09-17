class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)

        for source, destination, price in flights:
            adj[source].append((destination, price))

        minHeap = [(0, src, 0)]
        maxFlight = k + 1

        best = [[float("inf")] * (maxFlight + 1) for _ in range(n)]
        best[src][0] = 0

        while minHeap:
            price, city, flight = heapq.heappop(minHeap)

            if city == dst:
                return price
            
            if flight == maxFlight:
                continue
            if price > best[city][flight]:
                continue
            
            for nex, fliP, in adj[city]:
                nextPri = price + fliP
                nextFlightUse = flight + 1

                if nextPri < best[nex][nextFlightUse]:
                    best[nex][nextFlightUse] = nextPri

                    heapq.heappush(minHeap, (nextPri, nex, nextFlightUse))
        
        return -1
