from typing import List

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]) -> int:
        obstacles_set = set(map(tuple, obstacles))
        dx = [0, 1, 0, -1]  # directions - north, east, south, west
        dy = [1, 0, -1, 0]
        x = y = di = ans = 0
        
        for command in commands:
            if command == -2:  # turn left
                di = (di - 1) % 4
            elif command == -1:  # turn right
                di = (di + 1) % 4
            else:  # move forward
                for _ in range(command):
                    if (x + dx[di], y + dy[di]) not in obstacles_set:
                        x += dx[di]
                        y += dy[di]
                        ans = max(ans, x*x + y*y)
        
        return ans