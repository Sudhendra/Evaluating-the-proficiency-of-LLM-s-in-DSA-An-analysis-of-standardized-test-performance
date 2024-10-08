class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dx = [0, 1, 0, -1]  # defines direction changes on x-axis
        dy = [1, 0, -1, 0]  # defines direction changes on y-axis
        x = y = di = 0  # initial position at (0, 0) facing north
        obstacles = set(map(tuple, obstacles))
        ans = 0
        for cmd in commands:
            if cmd == -2:
                di = (di - 1) % 4 # turn left
            elif cmd == -1:
                di = (di + 1) % 4 # turn right
            else:
                for _ in range(cmd):
                    if (x + dx[di], y + dy[di]) not in obstacles:
                        x += dx[di]
                        y += dy[di]
                        ans = max(ans, x*x + y*y)
        return ans