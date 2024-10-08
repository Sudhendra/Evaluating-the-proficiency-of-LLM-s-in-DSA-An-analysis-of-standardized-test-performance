from typing import List

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        target = (1, 2, 3, 4, 5, 0)
        start = tuple(board[0] + board[1])
        visited = set()
        queue = [(start, 0)]

        while queue:
            state, moves = queue.pop(0)
            if state == target:
                return moves

            if state in visited:
                continue

            visited.add(state)
            zero_idx = state.index(0)
            next_states = []

            if zero_idx == 0:
                next_states = [(1, 0, 2, 3, 4, 5)]
            elif zero_idx == 1:
                next_states = [(0, 1, 2, 3, 4, 5), (1, 2, 0, 3, 4, 5)]
            elif zero_idx == 2:
                next_states = [(1, 2, 3, 0, 4, 5)]
            elif zero_idx == 3:
                next_states = [(3, 1, 2, 4, 0, 5)]
            elif zero_idx == 4:
                next_states = [(3, 1, 2, 0, 5, 4), (1, 0, 2, 3, 5, 4)]
            elif zero_idx == 5:
                next_states = [(3, 1, 2, 4, 5, 0)]

            for ns in next_states:
                new_state = list(state)
                new_state[zero_idx], new_state[ns.index(0)] = ns.index(0), 0
                queue.append((tuple(new_state), moves + 1))

        return -1
