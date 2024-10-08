from typing import List

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        exclusive_time = [0] * n
        prev_time = 0

        for log in logs:
            function_id, action, timestamp = log.split(':')
            function_id, timestamp = int(function_id), int(timestamp)

            if action == 'start':
                if stack:
                    exclusive_time[stack[-1]] += timestamp - prev_time
                stack.append(function_id)
                prev_time = timestamp
            else:
                exclusive_time[stack.pop()] += timestamp - prev_time + 1
                prev_time = timestamp + 1

        return exclusive_time
