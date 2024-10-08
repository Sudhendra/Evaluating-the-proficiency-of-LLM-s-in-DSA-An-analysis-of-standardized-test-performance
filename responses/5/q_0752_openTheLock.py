from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        
        deadends = set(deadends)
        visited = set(["0000"])
        queue = [("0000", 0)]
        
        while queue:
            current, turns = queue.pop(0)
            
            if current == target:
                return turns
            
            if current in deadends:
                continue
            
            for i in range(4):
                for j in [-1, 1]:
                    new_digit = str((int(current[i]) + j) % 10)
                    new_str = current[:i] + new_digit + current[i+1:]
                    
                    if new_str not in visited:
                        visited.add(new_str)
                        queue.append((new_str, turns+1))
        
        return -1
