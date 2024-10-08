from typing import List

class Solution:
    def gridIllumination(
        self, n: int, lamps: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        rows = set()
        cols = set()
        diag1 = set()
        diag2 = set()
        lamps_on = set()

        for r, c in lamps:
            rows.add(r)
            cols.add(c)
            diag1.add(r+c)
            diag2.add(r-c)

            lamps_on.add((r, c))

        def is_illuminated(row, col):
            return row in rows or col in cols or (row+col) in diag1 or (row-col) in diag2

        def turn_off_lamps(row, col):
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    nr, nc = row + dr, col + dc
                    if (nr, nc) in lamps_on:
                        lamps_on.remove((nr, nc))
                        rows.remove(nr)
                        cols.remove(nc)
                        diag1.remove(nr+nc)
                        diag2.remove(nr-nc)

        result = []
        for row, col in queries:
            result.append(1 if is_illuminated(row, col) else 0)
            turn_off_lamps(row, col)

        return result
