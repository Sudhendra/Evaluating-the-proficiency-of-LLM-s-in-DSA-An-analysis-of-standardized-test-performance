from typing import List

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])  # Sort courses by their deadlines
        heap = []  # Heap to store durations of courses taken
        total_time = 0

        for duration, deadline in courses:
            if total_time + duration <= deadline:  # If current course can be taken within deadline
                total_time += duration
                heapq.heappush(heap, -duration)  # Use negative duration for max heap
            elif heap and -heap[0] > duration:  # If current course has shorter duration than longest course in heap
                total_time += duration + heapq.heappop(heap)  # Replace longest course with current course
                heapq.heappush(heap, -duration)

        return len(heap)
