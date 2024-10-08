class Solution:
    def leastBricks(self, wall: List[List[int]) -> int:
        count = {}
        max_count = 0

        for row in wall:
            width_sum = 0
            for i in range(len(row) - 1):
                width_sum += row[i]
                count[width_sum] = count.get(width_sum, 0) + 1
                max_count = max(max_count, count[width_sum])

        return len(wall) - max_count