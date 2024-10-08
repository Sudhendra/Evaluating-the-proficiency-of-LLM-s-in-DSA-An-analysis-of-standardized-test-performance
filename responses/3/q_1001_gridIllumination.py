from collections import Counter

class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        lamps_set = set((r, c) for r, c in lamps)
        row_count = Counter(r for r, _ in lamps)
        col_count = Counter(c for _, c in lamps)
        diag_count = Counter(r - c for r, c in lamps)
        anti_diag_count = Counter(r + c for r, c in lamps)
        
        def is_illuminated(r, c):
            return row_count[r] > 0 or col_count[c] > 0 or diag_count[r - c] > 0 or anti_diag_count[r + c] > 0
        
        ans = []
        for r, c in queries:
            if is_illuminated(r, c):
                ans.append(1)
            else:
                ans.append(0)
            for dr in range(-1, 2):
                for dc in range(-1, 2):
                    nr, nc = r+dr, c+dc
                    if (nr, nc) in lamps_set:
                        lamps_set.remove((nr, nc))
                        row_count[nr] -= 1
                        col_count[nc] -= 1
                        diag_count[nr - nc] -= 1
                        anti_diag_count[nr + nc] -= 1
        
        return ans
