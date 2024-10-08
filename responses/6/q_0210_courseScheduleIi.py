from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for course, pre_course in prerequisites:
            graph[pre_course].append(course)
            indegree[course] += 1

        queue = [course for course in range(numCourses) if indegree[course] == 0]
        result = []

        while queue:
            node = queue.pop(0)
            result.append(node)

            for next_course in graph[node]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)

        return result if len(result) == numCourses else []
