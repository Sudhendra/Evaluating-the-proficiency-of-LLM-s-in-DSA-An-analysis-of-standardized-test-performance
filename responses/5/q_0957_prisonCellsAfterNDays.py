from typing import List

class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        seen = {}
        fast_forward = False
        while n > 0:
            if not fast_forward:
                state_key = tuple(cells)
                if state_key in seen:
                    n %= seen[state_key] - n
                    fast_forward = True
                else:
                    seen[state_key] = n

            if n > 0:
                n -= 1
                next_day = [0] + [cells[i-1] ^ cells[i+1] ^ 1 for i in range(1, 7)] + [0]
                cells = next_day

        return cells
