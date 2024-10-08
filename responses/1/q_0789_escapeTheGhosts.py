class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        player_distance = abs(target[0]) + abs(target[1])
        
        for ghost_position in ghosts:
            ghost_distance = abs(ghost_position[0] - target[0]) + abs(ghost_position[1] - target[1])
            if ghost_distance <= player_distance:
                return False
        
        return True