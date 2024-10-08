from collections import deque

class Solution:
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        in_degree = [0] * numCourses
        
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1
        
        queue = deque([course for course in range(numCourses) if in_degree[course] == 0])
        
        while queue:
            current_course = queue.popleft()
            numCourses -= 1
            
            for neighbor in graph[current_course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return numCourses == 0
