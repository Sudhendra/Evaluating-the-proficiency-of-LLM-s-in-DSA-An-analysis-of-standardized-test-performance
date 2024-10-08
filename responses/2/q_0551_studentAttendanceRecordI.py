class Solution:
    def checkRecord(self, s: str) -> bool:
        absent_count = 0
        late_count = 0

        for i in range(len(s)):
            if s[i] == 'A':
                absent_count += 1
                late_count = 0
                if absent_count >= 2:
                    return False
            elif s[i] == 'L':
                late_count += 1
                if late_count >= 3:
                    return False
            else:
                late_count = 0

        return True