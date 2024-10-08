from typing import List

class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        seen = {}
        while n > 0:
            cells_tuple = tuple(cells)
            if cells_tuple in seen:
                cycle_length = seen[cells_tuple] - n
                n %= cycle_length
            else:
                seen[cells_tuple] = n

            next_cells = [0] * 8
            for i in range(1, 7):
                if cells[i-1] == cells[i+1]:
                    next_cells[i] = 1
                else:
                    next_cells[i] = 0
            cells = next_cells
            n -= 1

        return cells
