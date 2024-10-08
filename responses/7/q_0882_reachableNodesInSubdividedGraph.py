from collections import defaultdict
import heapq

class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        graph = defaultdict(dict)
        for u, v, cnt in edges:
            graph[u][v] = cnt
            graph[v][u] = cnt

        pq = [(-maxMoves, 0)]
        dist = {}

        while pq:
            moves, node = heapq.heappop(pq)
            moves = -moves

            if node in dist:
                continue

            dist[node] = moves

            for nei, cost in graph[node].items():
                if moves >= cost and nei not in dist:
                    heapq.heappush(pq, (-(moves + cost + 1), nei))

        ans = len(dist)

        for u, v, cnt in edges:
            ans += min(cnt, max(0, maxMoves - dist.get(u, 0)) + max(0, maxMoves - dist.get(v, 0)))

        return ans
