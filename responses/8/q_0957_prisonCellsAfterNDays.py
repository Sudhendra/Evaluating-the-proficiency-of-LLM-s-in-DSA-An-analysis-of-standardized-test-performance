from typing import List

class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        def next_day(cells):
            new_cells = [0] * 8
            for i in range(1, 7):
                new_cells[i] = 1 if cells[i-1] == cells[i+1] else 0
            return new_cells
        
        seen = {}
        is_fast_forwarded = False
        while n > 0:
            if not is_fast_forwarded:
                cell_state = tuple(cells)
                if cell_state in seen:
                    n %= seen[cell_state] - n
                    is_fast_forwarded = True
                else:
                    seen[cell_state] = n

            if n > 0:
                n -= 1
                cells = next_day(cells)
        
        return cells
