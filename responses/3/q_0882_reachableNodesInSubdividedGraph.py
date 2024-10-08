from heapq import heappush, heappop

class Solution:

    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        
        graph = {}
        for u, v, cnt in edges:
            if u not in graph:
                graph[u] = {}
            if v not in graph:
                graph[v] = {}
            graph[u][v] = graph[v][u] = cnt
        
        pq = [(-maxMoves, 0)]
        visited = {}
        reachable = {}

        while pq:
            moves, node = heappop(pq)
            if node in visited:
                continue
            visited[node] = -moves
            
            for neighbor, cnt in graph.get(node, {}).items():
                if neighbor not in visited:
                    moves_to_neighbor = -1 * moves - cnt - 1
                    if moves_to_neighbor > 0:
                        reachable[(node, neighbor)] = min(cnt, moves + cnt)
                        heappush(pq, (-moves_to_neighbor, neighbor))    
        
        res = len(visited)
        
        for u, v, cnt in edges:
            res += min(cnt, reachable.get((u, v), 0) + reachable.get((v, u), 0))
        
        return res
