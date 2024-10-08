from typing import List
import heapq

class Solution:
    def scheduleCourse(self, courses: List[List[int]) -> int:
        courses.sort(key=lambda x: x[1])  # Sort courses by their deadlines
        max_heap = []
        current_time = 0
        
        for duration, deadline in courses:
            if current_time + duration <= deadline:  # If we can finish the course before its deadline
                heapq.heappush(max_heap, -duration)  # Add the negative duration to max heap
                current_time += duration
            elif max_heap and -max_heap[0] > duration:  # If we can replace a longer course with the current course
                current_time += duration + heapq.heappop(max_heap)  # Replace the longest course with the current course

        return len(max_heap)
