from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if "0000" in deadends:
            return -1
        
        def get_neighbors(node):
            neighbors = []
            for i in range(4):
                for d in (-1, 1):
                    new_node = node[:i] + str((int(node[i]) + d) % 10) + node[i+1:]
                    if new_node not in deadends:
                        neighbors.append(new_node)
            return neighbors

        queue = [("0000", 0)]
        visited = set(["0000"])
        
        while queue:
            node, level = queue.pop(0)
            if node == target:
                return level
            for neighbor in get_neighbors(node):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, level+1))
        
        return -1
