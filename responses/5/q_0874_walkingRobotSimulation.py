class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]) -> int:
        obstacles_set = set(map(tuple, obstacles))
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # North, East, South, West
        curr_dir = 0  # Starting direction (North)
        
        x, y = 0, 0  # Initial position
        max_distance = 0
        dx, dy = directions[curr_dir]
        
        for command in commands:
            if command == -2:  # Turn left
                curr_dir = (curr_dir - 1) % 4
                dx, dy = directions[curr_dir]
            elif command == -1:  # Turn right
                curr_dir = (curr_dir + 1) % 4
                dx, dy = directions[curr_dir]
            else:  # Move forward `k` units
                for _ in range(command):
                    if (x + dx, y + dy) in obstacles_set:
                        break
                    x += dx
                    y += dy
                    max_distance = max(max_distance, x**2 + y**2)
        
        return max_distance