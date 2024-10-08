from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)
            in_degree[course] += 1

        queue = [course for course in range(numCourses) if in_degree[course] == 0]
        order = []

        while queue:
            node = queue.pop(0)
            order.append(node)
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return order if len(order) == numCourses else []

    def findOrderDFS(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for course, pre in prerequisites:
            graph[course].append(pre)

        visited = [0] * numCourses
        order = []

        def dfs(node):
            if visited[node] == -1:
                return False
            if visited[node] == 1:
                return True

            visited[node] = -1
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False

            visited[node] = 1
            order.append(node)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return order[::-1]
