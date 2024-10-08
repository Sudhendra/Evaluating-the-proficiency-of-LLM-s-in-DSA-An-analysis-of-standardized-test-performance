class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        seen = {}
        while n > 0:
            cell_key = tuple(cells)
            if cell_key in seen:
                cycle_length = seen[cell_key] - n
                n %= cycle_length
            else:
                seen[cell_key] = n

            if n > 0:
                n -= 1
                next_day = [0] + [cells[i - 1] ^ cells[i + 1] ^ 1 for i in range(1, 7)] + [0]
                cells = next_day

        return cells