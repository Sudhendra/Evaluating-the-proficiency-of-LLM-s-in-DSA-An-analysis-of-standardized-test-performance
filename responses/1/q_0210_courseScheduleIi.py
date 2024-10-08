from collections import defaultdict, deque

class Solution:
    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        for course, preq in prerequisites:
            graph[preq].append(course)
            in_degree[course] += 1
        
        queue = deque([course for course in range(numCourses) if in_degree[course] == 0])
        result = []
        
        while queue:
            course = queue.popleft()
            result.append(course)
            for next_course in graph[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)
        
        return result if len(result) == numCourses else []
