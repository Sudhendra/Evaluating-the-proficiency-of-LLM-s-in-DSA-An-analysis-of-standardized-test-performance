class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        def dfs(board, hand):
            if not board:
                return 0

            if not hand:
                return -1

            result = float('inf')
            i = 0
            while i < len(board):
                j = i
                while j < len(board) and board[j] == board[i]:
                    j += 1

                needed = 3 - (j - i)
                if hand.count(board[i]) >= needed:
                    next_board = self.shrink(board[:i] + board[j:])
                    next_hand = hand.replace(board[i] * needed, '')
                    subresult = dfs(next_board, next_hand)
                    if subresult != -1:
                        result = min(result, needed + subresult)

                i = j

            return result if result != float('inf') else -1

        return dfs(board, hand)

    def shrink(self, board):
        stack = []
        i = 0
        for ball in board:
            if stack and stack[-1][0] == ball:
                stack[-1][1] += 1
                if stack[-1][1] >= 3:
                    stack.pop()
            else:
                stack.append([ball, 1])

        return ''.join(ball * count for ball, count in stack)