from typing import List

class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        def distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        player_distance = distance([0, 0], target)
        for ghost in ghosts:
            ghost_distance = distance(ghost, target)
            if ghost_distance <= player_distance:
                return False
        return True
