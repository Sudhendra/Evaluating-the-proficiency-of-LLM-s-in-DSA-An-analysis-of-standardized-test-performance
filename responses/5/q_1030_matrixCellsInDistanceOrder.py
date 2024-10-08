from typing import List

class Solution:
    def allCellsDistOrder(
        self, rows: int, cols: int, rCenter: int, cCenter: int
    ) -> List[List[int]]:
        def distance(cell1, cell2):
            return abs(cell1[0] - cell2[0]) + abs(cell1[1] - cell2[1])

        center = (rCenter, cCenter)
        cells = [[r, c] for r in range(rows) for c in range(cols)]
        cells.sort(key=lambda x: distance(x, center))
        
        return cells
