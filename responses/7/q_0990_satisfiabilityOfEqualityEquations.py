    def equationsPossible(self, equations: List[str]) -> bool:
        parent = {}

        def find(x):
            if x not in parent:
                parent[x] = x
                return x
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                parent[root_x] = root_y

        for eq in equations:
            if eq[1] == "=":
                union(eq[0], eq[3])

        for eq in equations:
            if eq[1] == "!":
                if find(eq[0]) == find(eq[3]):
                    return False

        return True
