class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        total_passwords = k ** n
        seen = set()
        ans = []

        def dfs(node):
            nonlocal ans
            for x in map(str, range(k)):
                n_node = node + x
                if n_node not in seen:
                    seen.add(n_node)
                    dfs(n_node[1:])
                    ans.append(x)

        dfs('0' * (n-1))
        return ''.join(ans) + '0' * (n-1)
