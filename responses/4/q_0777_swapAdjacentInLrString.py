from collections import Counter

class Solution:
  
    def canTransform(self, start: str, end: str) -> bool:
        if Counter(start) != Counter(end):
            return False
        
        n = len(start)
        i = j = 0
        
        while i < n and j < n:
            while i < n and start[i] == 'X':
                i += 1
            while j < n and end[j] == 'X':
                j += 1
            
            if (i == n) != (j == n):
                return False
            
            if i < n and j < n:
                if start[i] != end[j] or (start[i] == 'L' and i < j) or (start[i] == 'R' and i > j):
                    return False
            
            i += 1
            j += 1
        
        return True
