from typing import List
from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        
        visited = set(deadends)
        queue = deque([('0000', 0)])
        
        while queue:
            current, turns = queue.popleft()
            if current == target:
                return turns
            
            for i in range(4):
                for move in (1, -1):
                    new_digit = (int(current[i]) + move) % 10
                    new_combo = current[:i] + str(new_digit) + current[i + 1:]
                    
                    if new_combo not in visited:
                        visited.add(new_combo)
                        queue.append((new_combo, turns + 1))
        
        return -1
