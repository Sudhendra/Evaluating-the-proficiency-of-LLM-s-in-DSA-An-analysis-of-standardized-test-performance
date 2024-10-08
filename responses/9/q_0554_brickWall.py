from collections import defaultdict

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edge_count = defaultdict(int)
        max_edges = 0

        for row in wall:
            edge = 0
            for brick in row[:-1]:
                edge += brick
                edge_count[edge] += 1
                max_edges = max(max_edges, edge_count[edge])

        return len(wall) - max_edges
