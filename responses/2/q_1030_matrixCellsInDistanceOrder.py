from typing import List

class Solution:
    def allCellsDistOrder(
        self, rows: int, cols: int, rCenter: int, cCenter: int
    ) -> List[List[int]]:
        distances = [(r, c, abs(r - rCenter) + abs(c - cCenter)) for r in range(rows) for c in range(cols)]
        distances.sort(key=lambda x: x[2])
        return [[x[0], x[1]] for x in distances]
