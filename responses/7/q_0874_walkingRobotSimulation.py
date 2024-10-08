class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacles_set = set(map(tuple, obstacles))
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y, direction, max_distance = 0, 0, 0, 0
        
        for command in commands:
            if command == -2:  # Turn left 90 degrees
                direction = (direction - 1) % 4
            elif command == -1:  # Turn right 90 degrees
                direction = (direction + 1) % 4
            else:  # Move forward k units
                dx, dy = directions[direction]
                for _ in range(command):
                    if (x + dx, y + dy) in obstacles_set:
                        break
                    x += dx
                    y += dy
                    max_distance = max(max_distance, x**2 + y**2)
        
        return max_distance
