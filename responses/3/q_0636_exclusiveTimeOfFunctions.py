from typing import List

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        exclusive_times = [0] * n
        stack = []
        prev_time = 0
        
        for log in logs:
            details = log.split(':')
            function_id, status, timestamp = int(details[0]), details[1], int(details[2])
            if status == 'start':
                if stack:
                    exclusive_times[stack[-1]] += timestamp - prev_time
                stack.append(function_id)
                prev_time = timestamp
            else:
                exclusive_times[stack.pop()] += timestamp - prev_time + 1
                prev_time = timestamp + 1
        
        return exclusive_times
