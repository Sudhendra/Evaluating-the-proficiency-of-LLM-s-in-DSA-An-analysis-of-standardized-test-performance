class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]) -> List[int]:
        def find(parent, i):
            if parent[i] == i:
                return i
            return find(parent, parent[i])

        def union(parent, rank, i, j):
            parent_i = find(parent, i)
            parent_j = find(parent, j)

            if rank[parent_i] < rank[parent_j]:
                parent[parent_i] = parent_j
            elif rank[parent_i] > rank[parent_j]:
                parent[parent_j] = parent_i
            else:
                parent[parent_i] = parent_j
                rank[parent_j] += 1

        def find_cycle(edges, ignore_edge):
            parent = [i for i in range(len(edges) + 1)]
            rank = [0] * (len(edges) + 1)

            for i, (u, v) in enumerate(edges):
                if i == ignore_edge:
                    continue
                if find(parent, u) == find(parent, v):
                    return [u, v]
                union(parent, rank, u, v)

            return []

        n = len(edges)
        parent_of = defaultdict(list)
        candidate_edges = []

        for i, (u, v) in enumerate(edges):
            if v in parent_of:
                candidate_edges.append([parent_of[v][0], v])
                candidate_edges.append([u, v])
            parent_of[v].append(u)

        if not candidate_edges:
            return find_cycle(edges, -1)

        for candidate_edge in candidate_edges:
            cycle = find_cycle(edges, edges.index(candidate_edge))
            if not cycle:
                return candidate_edge

        return []