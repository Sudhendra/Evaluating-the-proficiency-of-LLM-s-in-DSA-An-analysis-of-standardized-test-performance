```python
from typing import List
import heapq

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])  # Sort courses by their deadlines
        max_heap = []  # Use heap to keep track of the durations of courses we have taken
        current_time = 0  # Current time
        for duration, deadline in courses:
            if current_time + duration <= deadline:  # Check if we can finish the course within the deadline
                heapq.heappush(max_heap, -duration)  # Push negative duration to max_heap
                current_time += duration
            elif max_heap and -max_heap[0] > duration:  # Check if we can optimize schedule by swapping courses
                current_time += duration + heapq.heappop(max_heap)  # Swap course with the longest duration
                heapq.heappush(max_heap, -duration)
        return len(max_heap)
```

