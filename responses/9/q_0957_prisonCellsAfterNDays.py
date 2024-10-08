from typing import List

class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        seen = {}  # Mapping to store current pattern
        while n > 0:
            tmp_cells = cells.copy()  # Create a copy of the current state
            for i in range(1, len(cells) - 1):
                cells[i] = 1 if tmp_cells[i-1] == tmp_cells[i+1] else 0
            n -= 1
            pattern = tuple(cells)  # Convert to tuple for dictionary
            if pattern in seen:  # If cycle found, update n
                n %= seen[pattern] - n
            seen[pattern] = n
        return cells
