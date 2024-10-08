from typing import List
from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if "0000" in deadends:
            return -1
        
        queue = deque([("0000", 0)])
        visited = set(["0000"])
        
        while queue:
            current, steps = queue.popleft()
            
            if current == target:
                return steps
            
            if current in deadends:
                continue
            
            for i in range(4):
                for move in [-1, 1]:
                    next_digit = str((int(current[i]) + move) % 10)
                    next_combo = current[:i] + next_digit + current[i+1:]
                    if next_combo not in visited:
                        visited.add(next_combo)
                        queue.append((next_combo, steps + 1))
        
        return -1
