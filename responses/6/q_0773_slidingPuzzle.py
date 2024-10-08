from typing import List

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        target = (1, 2, 3, 4, 5, 0)
        start = tuple(board[0] + board[1])
        queue = [(start, start.index(0), 0)]
        visited = set([start])

        while queue:
            state, zero_idx, steps = queue.pop(0)

            if state == target:
                return steps

            for delta in (-1, 1, -3, 3):
                new_idx = zero_idx + delta

                if new_idx < 0 or new_idx >= 6:
                    continue

                new_state = list(state)
                new_state[zero_idx], new_state[new_idx] = new_state[new_idx], new_state[zero_idx]
                new_state = tuple(new_state)

                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, new_idx, steps + 1))

        return -1
