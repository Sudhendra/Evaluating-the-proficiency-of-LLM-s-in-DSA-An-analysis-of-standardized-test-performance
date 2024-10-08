class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacles_set = set(map(tuple, obstacles))
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        curr_pos = [0, 0]
        curr_dir = 0
        max_dist = 0
        
        for command in commands:
            if command == -2:  # Turn left 90 degrees
                curr_dir = (curr_dir - 1) % 4
            elif command == -1:  # Turn right 90 degrees
                curr_dir = (curr_dir + 1) % 4
            else:  # Move forwards
                for _ in range(command):
                    next_pos = [curr_pos[0] + directions[curr_dir][0], curr_pos[1] + directions[curr_dir][1]]
                    if tuple(next_pos) in obstacles_set:
                        break
                    curr_pos = next_pos
                    max_dist = max(max_dist, curr_pos[0]**2 + curr_pos[1]**2)
        
        return max_dist
