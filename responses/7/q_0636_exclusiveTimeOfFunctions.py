from typing import List

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        exclusive_times = [0] * n
        stack = []
        prev_timestamp = 0

        for log in logs:
            function_id, action, timestamp = log.split(':')
            function_id, timestamp = int(function_id), int(timestamp)

            if action == 'start':
                if stack:
                    exclusive_times[stack[-1]] += timestamp - prev_timestamp
                stack.append(function_id)
                prev_timestamp = timestamp
            else:
                exclusive_times[stack.pop()] += timestamp - prev_timestamp + 1
                prev_timestamp = timestamp + 1

        return exclusive_times
