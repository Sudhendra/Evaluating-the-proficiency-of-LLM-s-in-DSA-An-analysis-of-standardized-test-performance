from collections import defaultdict
import heapq

class Solution:
    def reachableNodes(self, edges, maxMoves, n):
        
        graph = defaultdict(dict)
        for u, v, cnt in edges:
            graph[u][v] = graph[v][u] = cnt
        
        pq = [(0, 0)]
        dist = {0: 0}
        count = 0
        
        while pq:
            d, node = heapq.heappop(pq)
            if d > dist[node]:
                continue
            count += 1
            for nei in graph[node]:
                new_dist = d + graph[node][nei] + 1
                if new_dist <= maxMoves and new_dist < dist.get(nei, maxMoves + 1):
                    heapq.heappush(pq, (new_dist, nei))
                    dist[nei] = new_dist
                count += min(graph[node][nei], maxMoves - d)
        
        return count


# Test cases
sol = Solution()
print(sol.reachableNodes([[0,1,10],[0,2,1],[1,2,2]], 6, 3))  # Output: 13
print(sol.reachableNodes([[0,1,4],[1,2,6],[0,2,8],[1,3,1]], 10, 4))  # Output: 23
print(sol.reachableNodes([[1,2,4],[1,4,5],[1,3,1],[2,3,4],[3,4,5]], 17, 5))  # Output: 1
