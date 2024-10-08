class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        repeat_count = 0
        s1_count, s2_count = 0, 0
        i = 0
        while s1_count < n1:
            if s1[i] == s2[s2_count]:
                s2_count += 1
                if s2_count == len(s2):
                    s2_count = 0
                    repeat_count += 1
            i = (i + 1) % len(s1)
            if i == 0:
                s1_count += 1
        return repeat_count // n2
