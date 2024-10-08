from typing import List

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])

        taken_courses = []
        current_time = 0

        for duration, last_day in courses:
            if current_time + duration <= last_day:
                taken_courses.append(duration)
                current_time += duration
            else:
                if taken_courses and max(taken_courses) > duration:
                    current_time -= max(taken_courses)
                    taken_courses.remove(max(taken_courses))
                    taken_courses.append(duration)
                    current_time += duration

        return len(taken_courses)
