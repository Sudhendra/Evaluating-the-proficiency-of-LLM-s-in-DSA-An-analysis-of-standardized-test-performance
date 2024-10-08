from typing import List

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        taken_courses = []
        time = 0

        for duration, end_day in courses:
            if time + duration <= end_day:
                taken_courses.append(duration)
                time += duration
            else:
                if taken_courses and max(taken_courses) > duration:
                    max_duration = max(taken_courses)
                    taken_courses.remove(max_duration)
                    taken_courses.append(duration)
                    time = time - max_duration + duration

        return len(taken_courses)
