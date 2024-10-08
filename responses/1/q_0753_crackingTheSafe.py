class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        total_combinations = k ** n
        visited = set()
        password = "0" * (n - 1)
        
        def dfs(node):
            nonlocal password
            if len(visited) == total_combinations:
                return True
            for i in range(k):
                new_password = password + str(i)
                if new_password not in visited:
                    visited.add(new_password)
                    password = password[1:] + str(i)
                    if dfs(password):
                        return True
                    visited.remove(new_password)
                    password = password[:-1]
            return False
        
        visited.add(password)
        dfs(password)
        
        return password