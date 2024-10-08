from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for course, pre_course in prerequisites:
            graph[pre_course].append(course)
            in_degree[course] += 1

        queue = [course for course in range(numCourses) if in_degree[course] == 0]

        while queue:
            current_course = queue.pop(0)
            numCourses -= 1

            for post_course in graph[current_course]:
                in_degree[post_course] -= 1
                if in_degree[post_course] == 0:
                    queue.append(post_course)

        return numCourses == 0
