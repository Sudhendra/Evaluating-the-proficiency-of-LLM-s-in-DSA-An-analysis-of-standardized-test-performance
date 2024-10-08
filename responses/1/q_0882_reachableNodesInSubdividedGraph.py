import heapq

class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        graph = {}
        for u, v, w in edges:
            if u not in graph:
                graph[u] = {}
            if v not in graph:
                graph[v] = {}
            graph[u][v] = graph[v][u] = w
        
        pq = [(-maxMoves, 0)]  # tuple: (-moves left, node)
        visited = {}
        
        while pq:
            moves_left, node = heapq.heappop(pq)
            if node in visited:
                continue
            
            visited[node] = -moves_left
            
            for nei, weight in graph.get(node, {}).items():
                if nei not in visited:
                    moves = -moves_left - weight - 1
                    if moves > 0:
                        heapq.heappush(pq, (-moves, nei))
        
        ans = len(visited)  # count nodes visited based on maxMoves
        
        for u, v, w in edges:
            ans += min(w, visited.get(u, 0) + visited.get(v, 0))
        
        return ans
