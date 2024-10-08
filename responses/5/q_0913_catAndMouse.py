class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:

        def dfs(m_pos, c_pos, player):
            if m_pos == c_pos:
                return 2
            if m_pos == 0:
                return 1
            if player == 1:  # Mouse's turn
                draw = True
                for n_pos in graph[m_pos]:
                    next_move = dfs(n_pos, c_pos, 2)
                    if next_move == 1:  # Mouse wins
                        return 1
                    if next_move != 2:  # Draw
                        draw = False
                return 2 if draw else 0
            else:  # Cat's turn
                draw = True
                for n_pos in graph[c_pos]:
                    if n_pos == 0:
                        continue
                    next_move = dfs(m_pos, n_pos, 1)
                    if next_move == 2:  # Cat wins
                        return 2
                    if next_move != 1:  # Draw
                        draw = False
                return 1 if draw else 0

        return dfs(1, 2, 1)