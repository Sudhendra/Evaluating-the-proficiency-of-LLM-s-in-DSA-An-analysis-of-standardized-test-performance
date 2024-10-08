from typing import List

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        target = [1, 2, 3, 4, 5, 0]
        start = board[0] + board[1]
        moves = 0
        queue = [(start, start.index(0))]
        visited = set()

        while queue:
            new_queue = []
            for state, pos in queue:
                visited.add(tuple(state))
                if state == target:
                    return moves
                for d in [-1, 1, -3, 3]:
                    new_pos = pos + d
                    if abs(new_pos // 3 - pos // 3) + abs(new_pos % 3 - pos % 3) != 1:
                        continue
                    if 0 <= new_pos < 6:
                        new_state = state[:]
                        new_state[pos], new_state[new_pos] = new_state[new_pos], new_state[pos]
                        if tuple(new_state) not in visited:
                            new_queue.append((new_state, new_pos))
            moves += 1
            queue = new_queue

        return -1
