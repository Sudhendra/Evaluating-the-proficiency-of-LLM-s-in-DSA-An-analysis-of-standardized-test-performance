class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        total_digits = k ** n
        visited = set()
        safe = []

        def dfs(node):
            for next_digit in range(k):
                new_password = node + str(next_digit)
                if new_password not in visited:
                    visited.add(new_password)
                    dfs(new_password[:-n])
                    safe.append(str(next_digit))

        initial_node = "0" * (n-1)
        dfs(initial_node)

        return "".join(safe[::-1] + [initial_node])

# Example usage
solution = Solution()
print(solution.crackSafe(1, 2))  # Output: "10"
print(solution.crackSafe(2, 2))  # Output: "01100"
