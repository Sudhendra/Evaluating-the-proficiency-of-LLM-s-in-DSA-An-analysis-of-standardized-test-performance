class Solution:
    def checkRecord(self, s: str) -> bool:
        a_count = 0
        l_count = 0
        for i, char in enumerate(s):
            if char == 'A':
                a_count += 1
                if a_count >= 2:
                    return False
            if char == 'L':
                l_count += 1
                if l_count >= 3 and s[i-1] == 'L' and s[i-2] == 'L':
                    return False
            else:
                l_count = 0
        return True
