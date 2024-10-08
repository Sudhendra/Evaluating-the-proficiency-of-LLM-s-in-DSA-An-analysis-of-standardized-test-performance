from heapq import heappop, heappush

class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        graph = {}
        for u, v, w in edges:
            if u not in graph:
                graph[u] = {}
            if v not in graph:
                graph[v] = {}
            graph[u][v] = w
            graph[v][u] = w

        reachable_nodes = {0: maxMoves}
        heap = [(0, 0)]

        visited = set()

        while heap:
            moves, node = heappop(heap)

            if node in visited:
                continue

            visited.add(node)

            for neighbor, weight in graph[node].items():
                if neighbor not in visited:
                    remaining_moves = maxMoves - moves - weight - 1
                    if remaining_moves >= 0:
                        if neighbor not in reachable_nodes or remaining_moves > reachable_nodes[neighbor]:
                            reachable_nodes[neighbor] = remaining_moves
                            heappush(heap, (maxMoves - remaining_moves, neighbor))

                    covered_nodes = min(maxMoves, moves + weight)
                    reachable_nodes[neighbor] = max(reachable_nodes.get(neighbor, 0), covered_nodes)

        total_reachable_nodes = len(visited)

        for u, v, w in edges:
            total_reachable_nodes += min(w, reachable_nodes.get(u, 0) + reachable_nodes.get(v, 0))

        return total_reachable_nodes
