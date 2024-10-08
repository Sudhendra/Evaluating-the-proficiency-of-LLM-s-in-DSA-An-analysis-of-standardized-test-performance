from typing import List

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        exclusive_times = [0] * n
        stack = []
        prev_time = 0
        
        for log in logs:
            fid, event, time = log.split(':')
            fid, time = int(fid), int(time)
            
            if event == 'start':
                if stack:
                    exclusive_times[stack[-1]] += time - prev_time
                stack.append(fid)
                prev_time = time
            else:
                exclusive_times[stack.pop()] += time - prev_time + 1
                prev_time = time + 1
         
        return exclusive_times
