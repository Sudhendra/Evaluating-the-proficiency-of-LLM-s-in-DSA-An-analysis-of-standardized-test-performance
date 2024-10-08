from typing import List

class Solution:

    def catMouseGame(self, graph: List[List[int]]) -> int:
        n = len(graph)
        DRAW, MOUSE, CAT = 0, 1, 2

        # Create the game state for DP
        dp = [[[0] * n for _ in range(n)] for _ in range(2 * n)]

        # Initialize base cases
        for m in range(n):
            for c in range(1, n):
                dp[0][m][c] = MOUSE
                dp[0][c][m] = CAT

        # Implement game rules
        for t in range(1, 2 * n):
            for m in range(n):
                for c in range(1, n):
                    mouse_turn = t % 2 == 0
                    if mouse_turn:
                        dp[t][m][c] = CAT
                        for m2 in graph[m]:
                            if dp[t-1][m2][c] == MOUSE or dp[t-1][m2][c] == DRAW:
                                dp[t][m][c] = MOUSE
                                break
                    else:
                        dp[t][m][c] = MOUSE
                        for c2 in graph[c]:
                            if c2 == 0:
                                continue
                            if dp[t-1][m][c2] == CAT or dp[t-1][m][c2] == DRAW:
                                dp[t][m][c] = CAT
                                break

                    if (m == 0 and dp[t][m][c] == MOUSE) or (m == c and dp[t][m][c] == CAT):
                        dp[t][m][c] = DRAW

                    if m == c:
                        for prev_m in range(n):
                            if dp[t-1][prev_m][c] == CAT:
                                dp[t][m][c] = CAT
                                break

        return dp[2 * n - 1][1][2]
