from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        visit = [0 for _ in range(numCourses)]
        
        for pair in prerequisites:
            course, pre = pair
            graph[course].append(pre)
        
        def dfs(course):
            if visit[course] == 1:
                return False
            if visit[course] == 2:
                return True
            
            visit[course] = 1
            for pre in graph[course]:
                if not dfs(pre):
                    return False
            visit[course] = 2
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True