class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        targets = {i: (n - 1 - i // n, i % n if (n - 1 - i // n) % 2 != n % 2 else n - 1 - i % n) for i in range(1, n * n + 1)}
        
        def get_position(num):
            r, c = targets[num]
            return board[r][c]
        
        visited = set()
        dq = deque([(1, 0)])
        
        while dq:
            num, moves = dq.popleft()
            if num == n * n:
                return moves
            
            for i in range(1, 7):
                if num + i <= n * n:
                    next_num = get_position(num + i)
                    if next_num != -1:
                        next_num = next_num
                    if next_num not in visited:
                        visited.add(next_num)
                        dq.append((next_num, moves + 1))
        
        return -1
