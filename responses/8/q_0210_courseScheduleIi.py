from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1

        queue = [course for course in range(numCourses) if in_degree[course] == 0]
        result = []

        while queue:
            node = queue.pop(0)
            result.append(node)
            for next_course in graph[node]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)

        return result if len(result) == numCourses else []
