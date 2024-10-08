from itertools import product

class Solution:
    
    def findMinStep(self, board: str, hand: str) -> int:
        def remove_consecutive(board):
            stack = []
            start = end = 0
            while end < len(board):
                if board[start] == board[end]:
                    end += 1
                else:
                    if end - start >= 3:
                        while stack and stack[-1][0] == board[start]:
                            count, color = stack.pop()
                            start -= count
                    else:
                        stack.append((end - start, board[start]))
                    start = end
            if end - start >= 3:
                while stack and stack[-1][0] == board[start]:
                    count, color = stack.pop()
                    start -= count
            else:
                stack.append((end - start, board[start]))
            return ''.join(ch for count, ch in stack)

        def backtrack(board, hand):
            if not board:
                return 0
            if not hand:
                return -1
            key = (board, hand)
            if key in memo:
                return memo[key]
            res = float('inf')
            for b, h in product(range(len(board)), range(len(hand))):
                new_board = remove_consecutive(board[:b] + hand[h] + board[b:])
                new_hand = hand[:h] + hand[h+1:]
                if new_board:
                    further_steps = backtrack(new_board, new_hand)
                    if further_steps != -1:
                        res = min(res, 1 + further_steps)
            memo[key] = res if res != float('inf') else -1
            return memo[key]

        memo = {}
        result = backtrack(board, hand)
        return result if result != float('inf') else -1
