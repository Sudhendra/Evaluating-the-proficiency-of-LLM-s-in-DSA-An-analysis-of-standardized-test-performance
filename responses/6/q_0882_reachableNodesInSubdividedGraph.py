from collections import defaultdict
import heapq

class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        graph = defaultdict(dict)
        for u, v, cnt in edges:
            graph[u][v] = graph[v][u] = cnt
        
        max_moves = [0] * n
        visited = set()
        pq = [(-maxMoves, 0)]
        
        while pq:
            moves, node = heapq.heappop(pq)
            if node in visited:
                continue
            visited.add(node)
            
            max_moves[node] = -moves
            
            for neighbor, cnt in graph[node].items():
                if node not in visited and moves + cnt + 1 < maxMoves[neighbor]:
                    heapq.heappush(pq, (moves + cnt + 1, neighbor))
                    
        result = len(visited)
        
        for u, v, cnt in edges:
            result += min(cnt, maxMoves[u] + maxMoves[v])
        
        return result
