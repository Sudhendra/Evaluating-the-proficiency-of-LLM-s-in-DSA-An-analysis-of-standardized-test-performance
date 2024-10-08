from typing import List

class Solution:
    def allCellsDistOrder(
        self, rows: int, cols: int, rCenter: int, cCenter: int
    ) -> List[List[int]]:
        distances = [(r, c, abs(r - rCenter) + abs(c - cCenter)) for r in range(rows) for c in range(cols)]
        distances.sort(key=lambda x: x[2])
        return [[r, c] for r, c, _ in distances]

# Time complexity analysis:
# Generating all distances takes O(rows * cols) time.
# Sorting distances array takes O((rows * cols) * log(rows * cols)) time.
# Constructing the final result array takes O(rows * cols) time.
# Hence, the overall time complexity is O((rows * cols) * log(rows * cols)).
# The space complexity is also O(rows * cols) for the distances array and the result array.
