class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        seen = {}
        while n > 0:
            cell_tuple = tuple(cells)
            if cell_tuple in seen:
                cycle_length = seen[cell_tuple] - n
                n %= cycle_length
            seen[cell_tuple] = n

            next_day_cells = [0] * 8
            for i in range(1, 7):
                next_day_cells[i] = 1 if cells[i - 1] == cells[i + 1] else 0
            cells = next_day_cells
            n -= 1

        return cells