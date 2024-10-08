class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        if s1 == s2:
            return 0
        
        queue = collections.deque([s1])
        visited = {s1}
        target = s2
        k = 0
        
        while queue:
            size = len(queue)
            for _ in range(size):
                current = queue.popleft()
                if current == target:
                    return k
                
                i = 0
                while current[i] == target[i]:
                    i += 1
                
                for j in range(i+1, len(current)):
                    if current[j] == target[j] or current[j] != target[i]:
                        continue
                    
                    new_str = list(current)
                    new_str[i], new_str[j] = new_str[j], new_str[i]
                    new_str = "".join(new_str)
                    
                    if new_str not in visited:
                        queue.append(new_str)
                        visited.add(new_str)
                        
            k += 1
        
        return -1
