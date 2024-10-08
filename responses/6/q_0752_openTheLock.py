from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def neighbors(node):
            for i in range(4):
                for j in [-1, 1]:
                    yield node[:i] + str((int(node[i]) + j) % 10) + node[i+1:]

        dead_set = set(deadends)
        if "0000" in dead_set:
            return -1
        
        visited = set(["0000"])
        queue = [("0000", 0)]
        
        while queue:
            node, turns = queue.pop(0)
            if node == target:
                return turns
            
            for nei in neighbors(node):
                if nei not in visited and nei not in dead_set:
                    visited.add(nei)
                    queue.append((nei, turns + 1))
        
        return -1
