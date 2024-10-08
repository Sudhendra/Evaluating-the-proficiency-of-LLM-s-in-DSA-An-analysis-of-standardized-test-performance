class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        def remove_matches(board):
            stack = []
            start, end = 0, 0
            while end < len(board):
                if board[end] == board[start]:
                    end += 1
                else:
                    if end - start >= 3:
                        stack.append(board[:start] + board[end:])
                    start = end
            if end - start >= 3:
                stack.append(board[:start])
            return stack

        def backtrack(board, hand):
            if not board:
                return 0
            if not hand:
                return -1

            min_steps = float('inf')
            for i in range(len(hand)):
                for j in range(len(board)+1):
                    new_board = board[:j] + hand[i] + board[j:]
                    for new_board_updated in remove_matches(new_board):
                        next_hand = hand[:i] + hand[i+1:]
                        next_steps = backtrack(new_board_updated, next_hand)
                        
                        if next_steps != -1:
                            min_steps = min(min_steps, 1 + next_steps)

            return min_steps if min_steps != float('inf') else -1

        result = backtrack(board, hand)
        return result if result != float('inf') else -1
