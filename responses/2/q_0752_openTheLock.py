class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def neighbors(node):
            for i in range(4):
                x = int(node[i])
                for d in (-1, 1):
                    y = (x + d) % 10
                    yield node[:i] + str(y) + node[i+1:]

        dead = set(deadends)
        if "0000" in dead:
            return -1
        
        queue = deque([("0000", 0)])
        visited = {"0000"}

        while queue:
            node, level = queue.popleft()
            if node == target:
                return level
            
            for neighbor in neighbors(node):
                if neighbor not in visited and neighbor not in dead:
                    visited.add(neighbor)
                    queue.append((neighbor, level + 1))
        
        return -1