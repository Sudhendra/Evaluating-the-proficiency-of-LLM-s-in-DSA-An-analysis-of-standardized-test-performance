from typing import List

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        target = [1, 2, 3, 4, 5, 0]
        start = tuple(board[0] + board[1])
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = [(start, start.index(0), 0)]
        visited = {start}

        while queue:
            state, zero_idx, depth = queue.pop(0)
            if state == tuple(target):
                return depth

            for dx, dy in moves:
                new_zero_idx = zero_idx + dx + 3 * dy
                if 0 <= new_zero_idx < 6:
                    new_state = list(state)
                    new_state[zero_idx], new_state[new_zero_idx] = new_state[new_zero_idx], new_state[zero_idx]
                    new_state = tuple(new_state)

                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_state, new_zero_idx, depth + 1))

        return -1