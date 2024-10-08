from typing import List
import heapq

class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        graph = {}
        for u, v, cnt in edges:
            graph.setdefault(u, []).append((v, cnt))
            graph.setdefault(v, []).append((u, cnt))

        pq = [(-maxMoves, 0)]
        dist = {0: maxMoves}

        while pq:
            moves, node = heapq.heappop(pq)
            moves = -moves

            if moves < dist[node]:
                continue

            for nei, cnt in graph.get(node, []):
                new_moves = moves - cnt - 1
                if new_moves >= 0 and new_moves > dist.get(nei, -1):
                    dist[nei] = new_moves
                    heapq.heappush(pq, (-new_moves, nei))

        ans = len(dist)
        for u, v, cnt in edges:
            uv_dist = min(cnt, maxMoves - dist[u])
            vu_dist = min(cnt, maxMoves - dist[v])
            ans += min(uv_dist + vu_dist, cnt)

        return ans
