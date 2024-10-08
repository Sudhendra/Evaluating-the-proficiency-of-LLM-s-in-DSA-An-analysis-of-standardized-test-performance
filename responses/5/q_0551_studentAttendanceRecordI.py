class Solution:
    def checkRecord(self, s: str) -> bool:
        absent_count = 0
        late_count = 0
        
        for i, char in enumerate(s):
            if char == 'A':
                absent_count += 1
                late_count = 0
            elif char == 'L':
                late_count += 1
            else:
                late_count = 0
            
            if absent_count >= 2 or late_count >= 3:
                return False
        
        return True
