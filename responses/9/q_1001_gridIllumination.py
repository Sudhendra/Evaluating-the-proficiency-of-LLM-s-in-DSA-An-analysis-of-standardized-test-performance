from typing import List

class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        rows, cols, diag1, diag2 = set(), set(), set(), set()
        lamp_positions = set()
        ans = []

        def is_illuminated(row, col):
            return row in rows or col in cols or (row - col) in diag1 or (row + col) in diag2

        def toggle_lamp(row, col):
            nonlocal lamp_positions
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    nr, nc = row + dr, col + dc
                    if (nr, nc) in lamp_positions:
                        lamp_positions.remove((nr, nc))

        for row, col in lamps:
            rows.add(row)
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            lamp_positions.add((row, col))

        for query in queries:
            row, col = query
            if is_illuminated(row, col):
                ans.append(1)
            else:
                ans.append(0)

            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    nr, nc = row + dr, col + dc
                    if (nr, nc) in lamp_positions:
                        toggle_lamp(nr, nc)

        return ans
