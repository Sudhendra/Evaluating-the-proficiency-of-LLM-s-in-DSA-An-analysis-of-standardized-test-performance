class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        def is_cyclic(node, visited, rec_stack):
            visited[node] = True
            rec_stack[node] = True

            for nei in graph[node]:
                if not visited[nei]:
                    if is_cyclic(nei, visited, rec_stack):
                        return True
                elif rec_stack[nei]:
                    return True

            rec_stack[node] = False
            return False

        def dfs(node, visited, safe_nodes):
            if visited[node] == 1:
                return False
            if visited[node] == 2:
                return True

            visited[node] = 1

            for nei in graph[node]:
                if not dfs(nei, visited, safe_nodes):
                    return False

            visited[node] = 2
            safe_nodes.append(node)
            return True

        n = len(graph)
        visited = [0] * n
        safe_nodes = []

        for i in range(n):
            if not visited[i]:
                if not is_cyclic(i, [False] * n, [False] * n):
                    dfs(i, visited, safe_nodes)

        return sorted(safe_nodes)