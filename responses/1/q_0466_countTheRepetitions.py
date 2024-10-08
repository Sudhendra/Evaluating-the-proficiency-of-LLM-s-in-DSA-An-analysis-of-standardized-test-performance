class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        repeats = [0] * (len(s2) + 1)
        next_index = [0] * (len(s2) + 1)
        j, count = 0, 0

        for k in range(1, n1 + 1):
            for i in range(len(s1)):
                if s1[i] == s2[j]:
                    j += 1
                    if j == len(s2):
                        j = 0
                        count += 1

            if k == n1:
                return count

            if j in next_index:
                prev_repeat = repeats[next_index.index(j)]
                pattern_len = count - prev_repeat
                remaining_len = n1 - k
                cycles = remaining_len // pattern_len
                count += cycles * (count - prev_repeat)
                k += cycles * pattern_len
            else:
                next_index[count] = j
                repeats[count] = count

        return count