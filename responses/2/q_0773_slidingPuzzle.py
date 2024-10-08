from typing import List
from collections import deque

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        start = tuple(board[0] + board[1])
        target = (1, 2, 3, 4, 5, 0)
        
        moves = [                     # Possible moves for each position
            [1, 3],                   # 0
            [0, 4, 2],                # 1
            [1, 5],                   # 2
            [0, 4],                   # 3
            [1, 3, 5],                # 4
            [2, 4],                   # 5
        ]
        
        queue = deque([(start, 0)])   # Using BFS to find the shortest path
        visited = set([start])        # To avoid revisiting the same state
        
        while queue:
            state, steps = queue.popleft()
            
            if state == target:
                return steps
            
            zero_idx = state.index(0)
            for move_idx in moves[zero_idx]:
                new_state = list(state)
                new_state[zero_idx], new_state[move_idx] = new_state[move_idx], new_state[zero_idx]
                new_state = tuple(new_state)
                
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, steps + 1))
        
        return -1
