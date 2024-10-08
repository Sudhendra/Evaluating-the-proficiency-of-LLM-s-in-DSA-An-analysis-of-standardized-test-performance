from typing import List

class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        def turn_on(row, col):
            rows[row] += 1
            cols[col] += 1
            diagonals_sum[row - col] += 1
            anti_diagonals_sum[row + col] += 1
            lamps_pos.add((row, col))

        def turn_off(row, col):
            rows[row] -= 1
            cols[col] -= 1
            diagonals_sum[row - col] -= 1
            anti_diagonals_sum[row + col] -= 1
            lamps_pos.remove((row, col))

        def is_illuminated(row, col):
            return rows[row] > 0 or cols[col] > 0 or diagonals_sum[row - col] > 0 or anti_diagonals_sum[row + col] > 0

        rows = [0] * n
        cols = [0] * n
        diagonals_sum = [0] * (2 * n - 1)
        anti_diagonals_sum = [0] * (2 * n - 1)
        lamps_pos = set()

        for lamp in lamps:
            turn_on(lamp[0], lamp[1])

        results = []

        for query in queries:
            row, col = query[0], query[1]
            results.append(1 if is_illuminated(row, col) else 0)

            for i in range(-1, 2):
                for j in range(-1, 2):
                    new_row, new_col = row + i, col + j
                    if (new_row, new_col) in lamps_pos:
                        turn_off(new_row, new_col)

        return results
