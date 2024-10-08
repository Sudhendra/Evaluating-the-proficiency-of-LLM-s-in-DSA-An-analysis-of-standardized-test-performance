from typing import List

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                parent[root_x] = root_y
        
        n = len(stones)
        parent = list(range(n))
        rows = {}
        cols = {}
        
        for i, (x, y) in enumerate(stones):
            if x in rows:
                union(i, rows[x])
            else:
                rows[x] = i
            if y in cols:
                union(i, cols[y])
            else:
                cols[y] = i
        
        return n - len({find(x) for x in parent})

# Instantiate the Solution class
sol = Solution()
# Call the function with a test case
result = sol.removeStones([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]])
# Print the result
print(result)
