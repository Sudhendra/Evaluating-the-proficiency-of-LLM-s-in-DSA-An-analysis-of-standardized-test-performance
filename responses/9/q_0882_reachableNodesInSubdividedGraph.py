from collections import defaultdict
import heapq

class Solution:
    def reachableNodes(self, edges, maxMoves, n):
        graph = defaultdict(dict)
        for u, v, cnt in edges:
            graph[u][v] = graph[v][u] = cnt

        pq = [(-maxMoves, 0)]
        dist = {}
        while pq:
            moves, node = heapq.heappop(pq)
            if node in dist:
                continue
            dist[node] = -moves

            for nei, cnt in graph[node].items():
                if nei not in dist and -moves - cnt - 1 > dist.get(nei, 0):
                    heapq.heappush(pq, (moves + cnt + 1, nei))

        res = len(dist)
        for u, v, cnt in edges:
            res += min(dist.get(u, 0) + dist.get(v, 0), cnt)

        return res
