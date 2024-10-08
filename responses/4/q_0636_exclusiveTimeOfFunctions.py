from typing import List

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        exclusive_times = [0] * n
        prev_timestamp = 0
        
        for log in logs:
            fid, event, timestamp = log.split(":")
            fid = int(fid)
            timestamp = int(timestamp)
            
            if event == 'start':
                if stack:
                    exclusive_times[stack[-1]] += timestamp - prev_timestamp
                stack.append(fid)
                prev_timestamp = timestamp
            else:
                exclusive_times[stack.pop()] += timestamp - prev_timestamp + 1
                prev_timestamp = timestamp + 1
        
        return exclusive_times
