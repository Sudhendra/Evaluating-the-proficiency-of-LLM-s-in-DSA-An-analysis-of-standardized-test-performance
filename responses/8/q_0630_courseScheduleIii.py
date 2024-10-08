from typing import List

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])  # Sort courses by end day
        current_day = 0
        count = 0
        for duration, end_day in courses:
            if current_day + duration <= end_day:
                current_day += duration
                count += 1
            else:
                max_duration = duration
                max_index = count
                for i in range(count):
                    if courses[i][0] > max_duration:
                        max_duration = courses[i][0]
                        max_index = i
                if courses[max_index][0] > duration:
                    current_day += duration - courses[max_index][0]
        return count
