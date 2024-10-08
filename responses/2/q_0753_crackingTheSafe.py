class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        total_combinations = k ** n
        visited = set()
        password = "0" * n

        def dfs(node):
            nonlocal password

            for i in range(k):
                new_node = node + str(i)
                if new_node not in visited:
                    visited.add(new_node)
                    password += str(i)
                    if len(visited) == total_combinations:
                        return True
                    if dfs(new_node[n:]):
                        return True
                    visited.remove(new_node)
                    password = password[:-1]

            return False

        dfs("0" * (n-1))
        return password