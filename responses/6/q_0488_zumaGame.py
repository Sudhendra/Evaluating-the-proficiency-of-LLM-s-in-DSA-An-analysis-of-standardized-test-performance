from collections import Counter

class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        def remove_consecutive(board):
            stack = []
            for ball in board:
                if not stack or stack[-1][0] != ball:
                    stack.append((ball, 1))
                else:
                    _, count = stack.pop()
                    count += 1
                    if count < 3:
                        stack.append((ball, count))
            return ''.join(ball * count for ball, count in stack)
        
        def dfs(board, hand):
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
                j = i
                while j < len(board) and board[j] == board[i]:
                    j += 1
                
                need = max(3 - (j - i), 0)
                if hand[board[i]] >= need:
                    new_hand = hand[:board[i]] + hand[board[i] + 1:]
                    new_board = board[:i] + board[j:]
                    next_result = dfs(remove_consecutive(new_board), new_hand)
                    if next_result != -1:
                        res = min(res, need + next_result)
                
                i = j
            
            memo[key] = res if res != float('inf') else -1
            return memo[key]
        
        counter_hand = Counter(hand)
        memo = {}
        
        return dfs(board, counter_hand)

