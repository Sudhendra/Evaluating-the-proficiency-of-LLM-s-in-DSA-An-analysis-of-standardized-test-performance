from typing import List

class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        n = len(graph)

        DRAW, MOUSE, CAT = 0, 1, 2

        # The state (t, x, y) represents the current state of the game.
        # t = 0 for MOUSE, t = 1 for CAT
        # x: the mouse's position (1 to n)
        # y: the cat's position (1 to n)
        dp = [[[None for _ in range(n)] for _ in range(n)] for _ in range(3)]

        # Counts the number of different levels of moves.
        degrees = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(3)]

        # Queue for checking levels with new possible moves.
        queue = []

        # Initialization of the game states.
        for i in range(1, n):
            for j in range(1, n):
                degrees[0][i][j] = len(graph[i]) + len(graph[j])
                degrees[1][i][j] = len(graph[i])
                degrees[2][i][j] = len(graph[j])

                if 0 in graph[j]:
                    degrees[1][i][j] -= 1

        for i in range(1, n):
            dp[MOUSE][i][i] = dp[CAT][i][i] = 1

            for t in range(1, 3):
                queue.append((t, i, i))

            dp[DRAW][i][i] = 2

            for p in graph[0]:
                dp[MOUSE][p][i] = 1
                dp[MOUSE][i][i] = 1

                queue.append((MOUSE, p, i))
                queue.append((MOUSE, i, i))

        while len(queue) != 0:
            t, x, y = queue.pop(0)

            for x0 in graph[x] if t == MOUSE else graph[y]:
                for t0 in range(1, 3):
                    if dp[t0][x0][y] is not None:
                        continue

                    if t == MOUSE and t0 == MOUSE:
                        if dp[DRAW][x0][y] == 2:
                            dp[t0][x0][y] = 1
                            queue.append((t0, x0, y))
                        elif dp[DRAW][x0][y] == 1:
                            degrees[t0][x0][y] -= 1

                            if degrees[t0][x0][y] == 0:
                                dp[t0][x0][y] = 2
                                queue.append((t0, x0, y))
                    elif t == CAT and t0 == CAT:
                        if dp[DRAW][x][x0] == 2:
                            dp[t0][x][x0] = 2
                            queue.append((t0, x, x0))
                        elif dp[DRAW][x][x0] == 1:
                            degrees[t0][x][x0] -= 1

                            if degrees[t0][x][x0] == 0:
                                dp[t0][x][x0] = 2
                                queue.append((t0, x, x0))
                    elif t == MOUSE and t0 == CAT:
                        if dp[DRAW][x0][y] == 2:
                            dp[t0][x0][y] = 2
                            queue.append((t0, x0, y))
                        elif dp[DRAW][x0][y] == 1:
                            degrees[t0][x0][y] -= 1

                            if degrees[t0][x0][y] == 0:
                                dp[t0][x0][y] = 2
                                queue.append((t0, x0, y))
                    elif t == CAT and t0 == MOUSE:
                        if dp[DRAW][x][x0] == 2:
                            dp[t0][x][x0] = 1
                            queue.append((t0, x, x0))
                        elif dp[DRAW][x][x0] == 1:
                            degrees[t0][x][x0] -= 1

                            if degrees[t0][x][x0] == 0:
                                dp[t0][x][x0] = 2
                                queue.append((t0, x, x0))

        return dp[MOUSE][1][2]
