from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1
        
        queue = deque([course for course in range(numCourses) if indegree[course] == 0])
        order = []
        
        while queue:
            current_course = queue.popleft()
            order.append(current_course)
            for course in graph[current_course]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    queue.append(course)
        
        return order if len(order) == numCourses else []
