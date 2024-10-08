from typing import List

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        target = (1, 2, 3, 4, 5, 0)
        start = tuple(board[0] + board[1])
        moves = {0: (1, 3), 1: (0, 2, 4), 2: (1, 5), 3: (0, 4), 4: (1, 3, 5), 5: (2, 4)}

        queue = [(start, start.index(0), 0)]
        visited = set()

        while queue:
            state, pos, step = queue.pop(0)

            if state == target:
                return step
            
            if state in visited:
                continue

            visited.add(state)

            for move in moves[pos]:
                new_state = list(state)
                new_state[pos], new_state[move] = new_state[move], new_state[pos]
                queue.append((tuple(new_state), move, step + 1))

        return -1
