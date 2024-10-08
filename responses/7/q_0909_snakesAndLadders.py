from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        target = n * n
        visited = set()
        
        def get_position(square):
            r, c = divmod(square - 1, n)
            if r % 2 == 1:
                return n - 1 - r, c
            return n - 1 - r, n - 1 - c
        
        queue = deque([(1, 0)])
        
        while queue:
            square, moves = queue.popleft()
            
            if square == target:
                return moves
            
            for i in range(1, 7):
                next_square = square + i
                
                if next_square > target:
                    break
                
                r, c = get_position(next_square)
                
                if board[r][c] != -1:
                    next_square = board[r][c]
                
                if next_square not in visited:
                    visited.add(next_square)
                    queue.append((next_square, moves + 1))
        
        return -1
