from typing import List

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        taken_courses = []
        time = 0

        for duration, end in courses:
            if time + duration <= end:
                taken_courses.append(duration)
                time += duration
            elif taken_courses and duration < max(taken_courses):
                max_duration = max(taken_courses)
                taken_courses.remove(max_duration)
                taken_courses.append(duration)
                time += duration - max_duration

        return len(taken_courses)
