from typing import List

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        target = [1, 2, 3, 4, 5, 0]
        start = board[0] + board[1]
        neighbors = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }
        
        queue = [(start, start.index(0), 0)]
        visited = set(start)
        
        while queue:
            state, zero_pos, moves = queue.pop(0)
            if state == target:
                return moves
            for neighbor in neighbors[zero_pos]:
                new_state = state[:]
                new_state[zero_pos], new_state[neighbor] = new_state[neighbor], new_state[zero_pos]
                new_tuple = tuple(new_state)
                if new_tuple not in visited:
                    queue.append((new_state, neighbor, moves + 1))
                    visited.add(new_tuple)
        
        return -1
