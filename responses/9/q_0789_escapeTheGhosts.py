from typing import List

class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        player_distance_to_target = abs(target[0]) + abs(target[1])
        
        for ghost in ghosts:
            ghost_distance_to_target = abs(ghost[0] - target[0]) + abs(ghost[1] - target[1])
            if ghost_distance_to_target <= player_distance_to_target:
                return False
        
        return True
