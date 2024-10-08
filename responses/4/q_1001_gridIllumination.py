class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        rows = collections.defaultdict(int)
        cols = collections.defaultdict(int)
        diag1 = collections.defaultdict(int)
        diag2 = collections.defaultdict(int)
        lamps_set = set()

        for lamp in lamps:
            r, c = lamp
            rows[r] += 1
            cols[c] += 1
            diag1[r-c] += 1
            diag2[r+c] += 1
            lamps_set.add((r, c))

        ans = []

        def is_illuminated(r, c):
            return rows[r] > 0 or cols[c] > 0 or diag1[r-c] > 0 or diag2[r+c] > 0

        def turn_off_adjacent_lamps(r, c):
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    nr, nc = r + dr, c + dc
                    if (nr, nc) in lamps_set:
                        lamps_set.remove((nr, nc))
                        rows[nr] -= 1
                        cols[nc] -= 1
                        diag1[nr-nc] -= 1
                        diag2[nr+nc] -= 1

        for query in queries:
            r, c = query
            ans.append(1 if is_illuminated(r, c) else 0)
            turn_off_adjacent_lamps(r, c)

        return ans
