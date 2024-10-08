class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        def removeConsecutive(board):
            stack = []
            i = 0
            while i < len(board):
                curr_color = board[i]
                count = 1
                while i + 1 < len(board) and board[i + 1] == curr_color:
                    i += 1
                    count += 1
                if count >= 3:
                    while stack and stack[-1][0] == curr_color:
                        count += stack.pop()[1]
                    if count < 3:
                        stack.append((curr_color, 3 - count))
                else:
                    stack.append((curr_color, count))
                i += 1

            return "".join(color * count for color, count in stack)

        def backtrack(board, hand, memo):
            if not board:
                return 0
            if hand == "":
                return -1

            if (board, hand) in memo:
                return memo[(board, hand)]

            result = float('inf')
            for i in range(len(hand)):
                for j in range(len(board)+1):
                    new_board = board[:j] + hand[i] + board[j:]
                    updated_board = removeConsecutive(new_board)
                    next_hand = hand[:i] + hand[i + 1:]
                    res = backtrack(updated_board, next_hand, memo)
                    if res != -1:
                        result = min(result, 1 + res)

            if result == float('inf'):
                memo[(board, hand)] = -1
            else:
                memo[(board, hand)] = result

            return memo[(board, hand)]

        memo = {}
        res = backtrack(board, hand, memo)
        return res if res != float('inf') else -1
