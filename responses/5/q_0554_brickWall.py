from collections import defaultdict

class Solution:
    def leastBricks(self, wall: List[List[int]) -> int:
        edges = defaultdict(int)
        max_edges = 0
        for row in wall:
            prefix_sum = 0
            for i in range(len(row) - 1):
                prefix_sum += row[i]
                edges[prefix_sum] += 1
                max_edges = max(max_edges, edges[prefix_sum])

        return len(wall) - max_edges
