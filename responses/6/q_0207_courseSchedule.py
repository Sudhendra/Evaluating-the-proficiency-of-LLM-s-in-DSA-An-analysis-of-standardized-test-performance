from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        visit = [0] * numCourses
        
        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)
        
        def dfs(course):
            if visit[course] == 1:
                return False
            if visit[course] == 2:
                return True
            
            visit[course] = 1
            for next_course in graph[course]:
                if not dfs(next_course):
                    return False
            visit[course] = 2
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True
