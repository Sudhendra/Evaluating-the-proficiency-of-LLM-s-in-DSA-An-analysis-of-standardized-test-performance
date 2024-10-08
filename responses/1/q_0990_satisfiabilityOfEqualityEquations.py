class Solution:
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
                parent[root_y] = root_x

        for equation in equations:
            if equation[1] == '=':
                union(equation[0], equation[3])

        for equation in equations:
            if equation[1] == '!' and find(equation[0]) == find(equation[3]):
                return False

        return True