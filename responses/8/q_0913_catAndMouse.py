from typing import List

class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        n = len(graph)

        # Define a memoization function
        def memo(cat_pos, mouse_pos, cat_turn):
            return cat_pos, mouse_pos, cat_turn

        # Initialize the memoization table
        memo_table = {}
        
        def dfs(cat_pos, mouse_pos, cat_turn):
            if cat_pos == mouse_pos:
                return 2
            if mouse_pos == 0:
                return 1
            if cat_pos == 0:
                return 2

            if cat_turn == 1:  # Cat's turn
                res = 2  # Assume Cat wins
                for next_cat_pos in graph[cat_pos]:
                    if next_cat_pos == 0:
                        return 2
                    new_mouse_pos = memo(next_cat_pos, mouse_pos, 0)
                    if new_mouse_pos not in memo_table:
                        res = min(res, dfs(next_cat_pos, mouse_pos, 0))
                return res
            else:  # Mouse's turn
                res = 1  # Assume Mouse wins
                for next_mouse_pos in graph[mouse_pos]:
                    new_cat_pos = memo(cat_pos, next_mouse_pos, 1)
                    if new_cat_pos not in memo_table:
                        res = max(res, dfs(cat_pos, next_mouse_pos, 1))
                return res

        return dfs(2, 1, 1)  # Start from Cat at node 2, Mouse at node 1, Cat's turn

# The solution logic needs to be filled in the catMouseGame method.
