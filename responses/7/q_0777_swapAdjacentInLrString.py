class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        if start.replace('X', '') != end.replace('X', ''):
            return False
        
        n = len(start)
        i = 0
        j = 0
        
        while i < n and j < n:
            # Find the next valid character in the start string
            while i < n and start[i] == 'X':
                i += 1
            
            # Find the next valid character in the end string
            while j < n and end[j] == 'X':
                j += 1
                
            if i == n or j == n:
                break
            
            if start[i] != end[j] or (start[i] == 'L' and i < j) or (start[i] == 'R' and i > j):
                return False
            
            i += 1
            j += 1
        
        return True
