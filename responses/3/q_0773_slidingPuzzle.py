from typing import List

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        target = [1, 2, 3, 4, 5, 0]
        start = board[0] + board[1]
        moves = [(1, 3), (0, 2, 4), (1, 5), (0, 4), (1, 3, 5), (2, 4)]
        queue = [(start, start.index(0), 0)]
        visited = set()
        
        while queue:
            state, pos, step = queue.pop(0)
            if state == target:
                return step
            if state in visited:
                continue
            visited.add(state)
            
            for neighbor in moves[pos]:
                new_state = state[:]
                new_state[pos], new_state[neighbor] = new_state[neighbor], new_state[pos]
                queue.append((new_state, neighbor, step + 1))
        
        return -1
