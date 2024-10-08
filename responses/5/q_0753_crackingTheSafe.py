class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        ans = "0" * n
        seen = set()
        seen.add(ans)
        target = k ** n

        def dfs(node):
            nonlocal ans, seen, target
            if len(seen) == target:
                return True
            for i in range(k):
                new_node = node + str(i)
                if new_node not in seen:
                    seen.add(new_node)
                    ans += str(i)
                    if dfs(new_node[1:]):
                        return True
                    seen.remove(new_node)
                    ans = ans[:-1]
            return False

        dfs("0" * (n - 1))
        return ans
