class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        indegree = {i: 0 for i in range(numCourses)}
        
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
        
        queue = []
        
        for course in graph:
            if indegree[course] == 0:
                queue.append(course)
        
        count = 0
        while queue:
            node = queue.pop(0)
            count += 1
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return count == numCourses
