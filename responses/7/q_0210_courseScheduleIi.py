from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Create adjacency list and indegree array
        graph = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        # Topological Sort using Kahn's algorithm
        queue = []
        order = []

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            course = queue.pop(0)
            order.append(course)

            for c in graph[course]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    queue.append(c)

        if len(order) == numCourses:
            return order
        else:
            return []

# Example usage
numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
solution = Solution()
result = solution.findOrder(numCourses, prerequisites)
print(result)
