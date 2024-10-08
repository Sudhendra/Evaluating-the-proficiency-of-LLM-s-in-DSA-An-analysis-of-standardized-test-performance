from collections import Counter

class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        def dfs(board, hand):
            if not board:
                return 0
            
            if not hand:
                return -1
            
            key = board + ',' + hand
            if key in memo:
                return memo[key]
            
            res = float('inf')
            i, j = 0, 0
            while i < len(board):
                j = i
                while j < len(board) and board[j] == board[i]:
                    j += 1
                
                need = 3 - (j - i)
                if hand[board[i]] >= need:
                    new_hand = hand[:board[i]] + hand[board[i] + 1:]
                    new_board = process(board[:i] + board[j:])
                    next_res = dfs(new_board, new_hand)
                    if next_res != -1:
                        res = min(res, need + next_res)
                
                i = j
            
            memo[key] = res if res != float('inf') else -1
            return memo[key]
        
        def process(board):
            i, j = 0, 0
            while i < len(board):
                j = i
                while j < len(board) and board[j] == board[i]:
                    j += 1
                
                if j - i >= 3:
                    return process(board[:i] + board[j:])
                
                i = j
            
            return board
        
        memo = {}
        hand = Counter(hand)
        res = dfs(board, hand)
        return res if res != float('inf') else -1
