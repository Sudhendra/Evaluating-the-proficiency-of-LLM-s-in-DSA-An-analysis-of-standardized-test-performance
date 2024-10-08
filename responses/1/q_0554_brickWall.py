from collections import defaultdict

class Solution:
    def leastBricks(self, wall: List[List[int]) -> int:
        edges_count = defaultdict(int)
        max_edges = 0

        for row in wall:
            edge = 0
            for i in range(len(row) - 1):
                edge += row[i]
                edges_count[edge] += 1
                max_edges = max(max_edges, edges_count[edge])
        
        return len(wall) - max_edges
