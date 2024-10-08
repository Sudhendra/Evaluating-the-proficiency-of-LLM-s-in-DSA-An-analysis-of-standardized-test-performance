from collections import defaultdict

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edges = defaultdict(int)

        for row in wall:
            length = 0
            for i in range(len(row) - 1):
                length += row[i]
                edges[length] += 1

        max_edges = 0
        for key in edges:
            max_edges = max(max_edges, edges[key])

        return len(wall) - max_edges
