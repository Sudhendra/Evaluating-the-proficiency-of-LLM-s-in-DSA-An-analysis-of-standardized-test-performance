from typing import List
import heapq

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])  # Sort the courses by their deadlines
        max_heap = []  # Max heap to keep track of durations of courses taken
        time = 0
        for duration, end in courses:
            if time + duration <= end:
                heapq.heappush(max_heap, -duration)
                time += duration
            elif max_heap and duration < -max_heap[0]:
                time += duration + heapq.heappop(max_heap)
                heapq.heappush(max_heap, -duration)
        return len(max_heap)