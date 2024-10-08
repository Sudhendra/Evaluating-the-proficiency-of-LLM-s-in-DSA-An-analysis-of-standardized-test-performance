from typing import List

class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        n = len(graph)
        DRAW, MOUSE, CAT = 0, 1, 2
        
        # Set initial state for every possible scenario
        dp = [[[None] * n for _ in range(n)] for _ in range(3)]
        
        # Initialize states where cat is at hole to draw
        for c in range(n):
            for m in range(n):
                dp[0][m][c] = (DRAW, m, c)
        
        # Helper function to check if mouse/cat can move to hole
        def canMoveToHole(who, pos):
            return pos != 0 if who == MOUSE else pos == 0
        
        # Recursive function to determine winner
        def dfs(t, m, c):
            if dp[t][m][c] is not None:
                return dp[t][m][c]
            
            if t == MOUSE:
                win = CAT
                for next_m in graph[m]:
                    if next_m == 0:
                        win = MOUSE
                        break
                    if next_m != c:
                        next_win = dfs(CAT, next_m, c)
                        if next_win == MOUSE:
                            win = MOUSE
                            break
                    else:
                        draw_found = True
                
                if win == CAT and not draw_found:
                    win = DRAW
            else:
                win = MOUSE
                for next_c in graph[c]:
                    if next_c != 0:
                        next_win = dfs(MOUSE, m, next_c)
                        if next_win == CAT:
                            win = CAT
                            break
                
            dp[t][m][c] = (win, m, c)
            return win
            
        return dfs(MOUSE, 1, 2)
