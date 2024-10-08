from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        target = n*n
        visited = set()
        
        def get_next(curr):
            r, c = divmod(curr - 1, n)
            row = n - 1 - r if r % 2 == 0 else r
            col = c if r % 2 == 0 else n - 1 - c
            return row, col
        
        queue = deque([(1, 0)])  # (position, moves)
        
        while queue:
            pos, moves = queue.popleft()
            if pos in visited:
                continue
            visited.add(pos)
            
            for i in range(1, 7):
                next_pos = pos + i
                if next_pos == target:
                    return moves + 1
                
                if next_pos > target:
                    break
                
                row, col = get_next(next_pos)
                
                if board[row][col] != -1:
                    next_pos = board[row][col]
                
                if next_pos not in visited:
                    queue.append((next_pos, moves + 1))
        
        return -1