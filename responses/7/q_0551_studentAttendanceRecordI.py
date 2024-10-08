class Solution:
    def checkRecord(self, s: str) -> bool:
        absences = 0
        lates = 0
        
        for i in range(len(s)):
            if s[i] == 'A':
                absences += 1
                lates = 0
            elif s[i] == 'L':
                lates += 1
            else:
                lates = 0
            
            if absences >= 2 or lates >= 3:
                return False
        
        return True
