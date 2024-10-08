from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(numCourses)}
        in_degree = {i: 0 for i in range(numCourses)}

        for course, preq in prerequisites:
            graph[preq].append(course)
            in_degree[course] += 1

        queue = deque([course for course in graph if in_degree[course] == 0])
        result = []

        while queue:
            course = queue.popleft()
            result.append(course)

            for next_course in graph[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)

        if len(result) == numCourses:
            return result
        return []
