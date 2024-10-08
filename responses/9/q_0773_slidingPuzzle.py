from typing import List

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        target = (1, 2, 3, 4, 5, 0)
        start = tuple(board[0] + board[1])

        neighbor_mapping = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }

        start_str = ''.join(map(str, start))
        target_str = ''.join(map(str, target))

        if start_str == target_str:
            return 0

        queue = [(start, 0)]
        visited = set([start])

        while queue:
            state, step = queue.pop(0)
            if state == target:
                return step

            pos_zero = state.index(0)
            for new_pos in neighbor_mapping[pos_zero]:
                new_state = list(state)
                new_state[pos_zero], new_state[new_pos] = new_state[new_pos], new_state[pos_zero]
                new_state_tuple = tuple(new_state)
                if new_state_tuple not in visited:
                    queue.append((new_state_tuple, step + 1))
                    visited.add(new_state_tuple)

        return -1
