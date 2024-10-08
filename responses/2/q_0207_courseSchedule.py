from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        indegree = {i: 0 for i in range(numCourses)}

        for course, pre_course in prerequisites:
            graph[pre_course].append(course)
            indegree[course] += 1

        queue = deque([course for course in graph if indegree[course] == 0])
        courses_taken = 0

        while queue:
            current_course = queue.popleft()
            courses_taken += 1
            for next_course in graph[current_course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)

        return courses_taken == numCourses
