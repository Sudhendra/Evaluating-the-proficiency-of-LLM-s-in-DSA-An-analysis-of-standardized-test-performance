from typing import List

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # North, East, South, West
        current_direction = 0  # Starting facing North
        x, y = 0, 0
        max_distance = 0
        obstacles = set(map(tuple, obstacles))
        
        for command in commands:
            if command == -2:  # Turn left
                current_direction = (current_direction - 1) % 4
            elif command == -1:  # Turn right
                current_direction = (current_direction + 1) % 4
            else:
                for _ in range(command):
                    next_x = x + directions[current_direction][0]
                    next_y = y + directions[current_direction][1]
                    if (next_x, next_y) in obstacles:
                        break
                    x, y = next_x, next_y
                    max_distance = max(max_distance, x**2 + y**2)
        
        return max_distance

# Example usage
sol = Solution()
print(sol.robotSim([4, -1, 3], []))  # Output: 25
print(sol.robotSim([4, -1, 4, -2, 4], [[2, 4]]))  # Output: 65
print(sol.robotSim([6, -1, -1, 6], []))  # Output: 36
