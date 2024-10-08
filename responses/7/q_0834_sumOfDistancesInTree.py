class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node, parent):
            subtree_size[node] = 1
            subtree_sum[node] = 0

            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                dfs(neighbor, node)
                subtree_size[node] += subtree_size[neighbor]
                subtree_sum[node] += subtree_sum[neighbor] + subtree_size[neighbor]

        def dfs_final(node, parent):
            result[node] = subtree_sum[node]
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                old_subtree_sum_node = subtree_sum[node]
                old_subtree_sum_neighbor = subtree_sum[neighbor]
                old_subtree_size_node = subtree_size[node]
                old_subtree_size_neighbor = subtree_size[neighbor]

                subtree_sum[node] -= subtree_sum[neighbor] + subtree_size[neighbor]
                subtree_size[node] -= subtree_size[neighbor]
                subtree_sum[neighbor] += subtree_sum[node] + subtree_size[node]
                subtree_size[neighbor] += subtree_size[node]

                dfs_final(neighbor, node)

                subtree_sum[node] = old_subtree_sum_node
                subtree_sum[neighbor] = old_subtree_sum_neighbor
                subtree_size[node] = old_subtree_size_node
                subtree_size[neighbor] = old_subtree_size_neighbor

        subtree_size = [0] * n
        subtree_sum = [0] * n
        result = [0] * n

        dfs(0, -1)
        dfs_final(0, -1)

        return result

# Test cases
solution = Solution()
print(solution.sumOfDistancesInTree(6, [[0,1],[0,2],[2,3],[2,4],[2,5]]))  # Output: [8, 12, 6, 10, 10, 10]
print(solution.sumOfDistancesInTree(1, []))  # Output: [0]
print(solution.sumOfDistancesInTree(2, [[1,0]]))  # Output: [1, 1]
