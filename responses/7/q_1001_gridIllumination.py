from collections import Counter

class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        def is_illuminated(row, col, lamps):
            for r, c in lamps:
                if r == row or c == col or abs(r-row) == abs(c-col):
                    return True
            return False
        
        def turn_off_lamps(row, col, lamps):
            for r, c in list(lamps):
                if r == row or c == col or abs(r-row) == abs(c-col):
                    lamps.remove((r,c))
        
        rows, cols, diagonals, lamps_set = Counter(), Counter(), Counter(), set()
        for lamp in lamps:
            r, c = lamp
            rows[r] += 1
            cols[c] += 1
            diagonals[r-c] += 1
            lamps_set.add((r,c))
        
        result = []
        for query in queries:
            row, col = query
            if rows[row] > 0 or cols[col] > 0 or diagonals[row-col] > 0:
                result.append(1)
            else:
                result.append(0)
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    new_row, new_col = row + dr, col + dc
                    if (new_row, new_col) in lamps_set:
                        turn_off_lamps(new_row, new_col, lamps_set)
                        rows[new_row] -= 1
                        cols[new_col] -= 1
                        diagonals[new_row-new_col] -= 1
        
        return result
