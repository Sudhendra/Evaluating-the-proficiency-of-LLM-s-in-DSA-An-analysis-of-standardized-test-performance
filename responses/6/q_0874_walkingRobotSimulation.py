from typing import List

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # north, east, south, west
        obstacles_set = set(map(tuple, obstacles))
        
        x, y = 0, 0
        direction_idx = 0
        max_distance = 0
        
        for command in commands:
            if command == -2:  # Turn left
                direction_idx = (direction_idx - 1) % 4
            elif command == -1:  # Turn right
                direction_idx = (direction_idx + 1) % 4
            else:  # Move forward
                dx, dy = directions[direction_idx]
                for _ in range(command):
                    if (x + dx, y + dy) not in obstacles_set:
                        x += dx
                        y += dy
                        max_distance = max(max_distance, x*x + y*y)
        return max_distance
