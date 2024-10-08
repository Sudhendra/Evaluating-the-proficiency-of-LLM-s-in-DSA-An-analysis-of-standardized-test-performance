import collections

class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        def dfs(board):
            if not board:
                return 0
            if not hand:
                return -1

            key = (board, hand)
            if key in memo:
                return memo[key]

            res = float('inf')
            i = 0
            while i < len(board):
                j = i + 1
                while j < len(board) and board[j] == board[i]:
                    j += 1

                need = 3 - (j - i)
                if hand[board[i]] >= need:
                    next_board = self.removeConsecutive(board[:i] + board[j:])
                    next_hand = hand.copy()
                    next_hand[board[i]] -= need
                    temp = dfs(next_board)
                    if temp >= 0:
                        res = min(res, temp + need)
                
                i = j
            
            memo[key] = res if res != float('inf') else -1
            return memo[key]

        def removeConsecutive(board):
            i = 0
            while i < len(board):
                j = i
                while j < len(board) and board[j] == board[i]:
                    j += 1

                if j - i >= 3:
                    return removeConsecutive(board[:i] + board[j:])

                i = j

            return board

        hand = collections.Counter(hand)
        memo = {}
        result = dfs(board)

        return result if result != float('inf') else -1
