class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ones_prefix = 0
        flips = 0
        
        for i in s:
            if i == '0':
                if ones_prefix == 0:
                    continue
                flips += 1
            else:
                ones_prefix += 1
            flips = min(flips, ones_prefix)
        
        return flips
