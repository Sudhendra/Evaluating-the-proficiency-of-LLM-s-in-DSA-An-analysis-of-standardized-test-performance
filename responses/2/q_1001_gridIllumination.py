from collections import defaultdict

class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        rows, cols, diags1, diags2, lamp_set = defaultdict(int), defaultdict(int), defaultdict(int), defaultdict(int), set()

        for r, c in lamps:
            rows[r] += 1
            cols[c] += 1
            diags1[r - c] += 1
            diags2[r + c] += 1
            lamp_set.add((r, c))

        def is_illuminated(r, c):
            return rows[r] > 0 or cols[c] > 0 or diags1[r - c] > 0 or diags2[r + c] > 0

        def turn_off_adjacent_lamps(r, c):
            directions = [(0, 0), (0, 1), (1, 0), (1, 1), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1)]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr, nc) in lamp_set:
                    rows[nr] -= 1
                    cols[nc] -= 1
                    diags1[nr - nc] -= 1
                    diags2[nr + nc] -= 1
                    lamp_set.remove((nr, nc))

        result = []
        for q in queries:
            r, c = q
            result.append(1 if is_illuminated(r, c) else 0)
            turn_off_adjacent_lamps(r, c)

        return result
