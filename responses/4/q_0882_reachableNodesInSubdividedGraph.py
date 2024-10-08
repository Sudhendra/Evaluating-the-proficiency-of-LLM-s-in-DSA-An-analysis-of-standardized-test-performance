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

        nodes_reachable = set()
        max_moves = [0] * n
        max_moves[0] = maxMoves
        
        heap = [(-maxMoves, 0)]
        
        while heap:
            moves, node = heappop(heap)
            moves = -moves

            if node in nodes_reachable:
                continue

            nodes_reachable.add(node)
            
            for neighbor, cnt in graph.get(node, {}).items():
                new_moves = moves - cnt - 1
                if new_moves >= 0 and new_moves > max_moves[neighbor]:
                    max_moves[neighbor] = new_moves
                    heappush(heap, (-new_moves, neighbor))
                nodes_reachable.add(neighbor)
        
        result = len(nodes_reachable)
        
        for u, v, cnt in edges:
            result += min(maxMoves, max_moves.get(u, 0) + max_moves.get(v, 0))
        
        return result
