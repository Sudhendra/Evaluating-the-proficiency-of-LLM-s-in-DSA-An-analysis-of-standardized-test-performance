class Solution:
    def snakesAndLadders(self, board):
        n = len(board)
        dest_to_row = lambda dest: n - 1 - (dest - 1) // n
        dest_to_col = lambda dest: (dest - 1) % n if dest_to_row(dest) % 2 != n % 2 else n - 1 - (dest - 1) % n

        visited = set()
        moves = 0
        queue = deque([(1, 0)])  # tuple: (current position, moves)

        while queue:
            curr, moves = queue.popleft()
            if curr in visited:
                continue
            visited.add(curr)
            if curr == n*n:
                return moves
            
            for i in range(1, 7):
                next_pos = curr + i
                if next_pos > n*n:
                    break
                row, col = dest_to_row(next_pos), dest_to_col(next_pos)
                next = board[row][col] if board[row][col] != -1 else next_pos
                queue.append((next, moves + 1))
        
        return -1