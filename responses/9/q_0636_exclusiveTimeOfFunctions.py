from typing import List

class Solution:
    
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        result = [0] * n
        stack = []
        prev_time = 0
        
        for log in logs:
            function_id, event, timestamp = log.split(':')
            function_id, timestamp = int(function_id), int(timestamp)
            
            if event == 'start':
                if stack:
                    result[stack[-1]] += timestamp - prev_time
                stack.append(function_id)
                prev_time = timestamp
            else:
                result[stack.pop()] += timestamp - prev_time + 1
                prev_time = timestamp + 1
        
        return result
