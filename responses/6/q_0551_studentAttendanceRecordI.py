class Solution:
    def checkRecord(self, s: str) -> bool:
        absent_count = 0
        late_streak = 0

        for i in range(len(s)):
            if s[i] == 'A':
                absent_count += 1
                late_streak = 0
            elif s[i] == 'L':
                late_streak += 1
            else:
                late_streak = 0

            if absent_count >= 2 or late_streak >= 3:
                return False

        return True
