from typing import List

class Solution:
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        visited = [0] * numCourses
        
        for course, pre_course in prerequisites:
            graph[course].append(pre_course)
        
        def has_cycle(course):
            if visited[course] == -1:
                return False
            if visited[course] == 1:
                return True
            
            visited[course] = -1
            for pre_course in graph[course]:
                if has_cycle(pre_course):
                    return True
            
            visited[course] = 1
            return False
        
        for course in range(numCourses):
            if has_cycle(course):
                return False
        
        return True