from typing import List

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x, y = 0, 0
        dx, dy = 0, 1
        obstacles_set = set(map(tuple, obstacles))
        max_distance = 0

        for command in commands:
            if command == -2:  # Turn left
                dx, dy = -dy, dx
            elif command == -1:  # Turn right
                dx, dy = dy, -dx
            else:
                for _ in range(command):
                    if (x + dx, y + dy) in obstacles_set:
                        break
                    x += dx
                    y += dy
                max_distance = max(max_distance, x**2 + y**2)

        return max_distance
