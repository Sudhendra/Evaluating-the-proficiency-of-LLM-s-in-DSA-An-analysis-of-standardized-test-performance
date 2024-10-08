from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        visited = set()
        target = n * n

        def get_coordinate(square):
            row = (square - 1) // n
            col = (square - 1) % n
            if row % 2 == 1:
                col = n - 1 - col
            return n - 1 - row, col

        def bfs():
            queue = deque([(1, 0)])
            while queue:
                square, moves = queue.popleft()
                if square in visited:
                    continue
                visited.add(square)
                
                if square == target:
                    return moves
                
                for i in range(1, 7):
                    if square + i <= target:
                        next_row, next_col = get_coordinate(square + i)
                        next_square = board[next_row][next_col] if board[next_row][next_col] != -1 else square + i
                        queue.append((next_square, moves + 1))
            return -1

        return bfs()
