from typing import List

class Solution:
    
    def allCellsDistOrder(
        self, rows: int, cols: int, rCenter: int, cCenter: int
    ) -> List[List[int]]:
        distances = [(r, c, abs(r - rCenter) + abs(c - cCenter)) for r in range(rows) for c in range(cols)]
        sorted_distances = sorted(distances, key=lambda x: x[2])
        return [[r, c] for r, c, _ in sorted_distances]

# Example usage
solution = Solution()
print(solution.allCellsDistOrder(1, 2, 0, 0))  # Output: [[0, 0], [0, 1]]
