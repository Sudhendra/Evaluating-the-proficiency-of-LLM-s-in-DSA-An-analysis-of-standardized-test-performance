from typing import List

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        def countBits(num):
            count = 0
            while num:
                num &= num - 1
                count += 1
            return count
        
        res = []
        for h in range(12):
            for m in range(60):
                if countBits(h) + countBits(m) == turnedOn:
                    res.append(f"{h}:{m:02d}")
        return res
