from typing import List

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dx = [0, 1, 0, -1]  # directions for x: north, east, south, west
        dy = [1, 0, -1, 0]  # directions for y: north, east, south, west

        obstacles_set = set(map(tuple, obstacles))
        x = y = d = res = 0

        for command in commands:
            if command == -2:  # Turn left
                d = (d - 1) % 4
            elif command == -1:  # Turn right
                d = (d + 1) % 4
            else:  # Move forward
                for _ in range(command):
                    nx, ny = x + dx[d], y + dy[d]
                    if (nx, ny) not in obstacles_set:
                        x, y = nx, ny
                        res = max(res, x*x + y*y)

        return res
