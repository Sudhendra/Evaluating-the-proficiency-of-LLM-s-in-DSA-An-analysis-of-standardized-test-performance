from typing import List

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        current_time = 0
        taken_courses = []

        for duration, end_time in courses:
            if current_time + duration <= end_time:
                taken_courses.append(duration)
                current_time += duration
            else:
                if taken_courses and duration < max(taken_courses):
                    current_time -= max(taken_courses)
                    taken_courses.remove(max(taken_courses))
                    taken_courses.append(duration)
                    current_time += duration

        return len(taken_courses)
