from typing import List

class Solution:
    
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        seen = {}
        while n > 0:
            cell_tuple = tuple(cells)
            if cell_tuple in seen:
                n %= seen[cell_tuple] - n
            seen[cell_tuple] = n
            
            if n >= 1:
                n -= 1
                next_day_cells = [0] * len(cells)
                for i in range(1, 7):
                    if cells[i-1] == cells[i+1]:
                        next_day_cells[i] = 1
                cells = next_day_cells
        
        return cells
