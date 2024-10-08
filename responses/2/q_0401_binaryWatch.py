from typing import List

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        def countBits(num):
            count = 0
            while num:
                count += num & 1
                num >>= 1
            return count
        
        def generateTimes(turnedOn, startIdx, hours, minutes, result):
            if turnedOn == 0:
                if hours < 12 and minutes < 60:
                    result.append(f"{hours}:{minutes:02d}")
                return
            
            for i in range(startIdx, 10):
                if i < 4:
                    next_hours = hours + (1 << i)
                    generateTimes(turnedOn - 1, i + 1, next_hours, minutes, result)
                else:
                    next_minutes = minutes + (1 << (i - 4))
                    generateTimes(turnedOn - 1, i + 1, hours, next_minutes, result)
        
        result = []
        generateTimes(turnedOn, 0, 0, 0, result)
        return result
