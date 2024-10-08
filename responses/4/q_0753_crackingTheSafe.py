def crackSafe(self, n: int, k: int) -> str:
    total_combinations = k ** n
    visited = set()
    safe_sequence = "0" * (n - 1)
    
    def dfs(node):
        nonlocal safe_sequence
        if len(visited) == total_combinations:
            return True
        
        for digit in range(k):
            new_node = node + str(digit)
            if new_node not in visited:
                visited.add(new_node)
                safe_sequence += str(digit)
                if dfs(new_node[1:]):
                    return True
                visited.remove(new_node)
                safe_sequence = safe_sequence[:-1]
        
        return False
    
    dfs(safe_sequence)
    return safe_sequence
