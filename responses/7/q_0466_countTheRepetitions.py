class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        repeatCount = 0
        s1_index, s2_index = 0, 0
        s1_len, s2_len = len(s1), len(s2)
        s1_dict, s2_dict = {}, {}

        while s1_index < n1 * s1_len:
            if s1[s1_index % s1_len] == s2[s2_index % s2_len]:
                s2_index += 1

                if s2_index % s2_len == 0:
                    repeatCount += 1

                if s1_index % s1_len not in s1_dict:
                    s1_dict[s1_index % s1_len] = (s2_index % s2_len, repeatCount)
                    s2_dict[s2_index % s2_len] = repeatCount
                else:
                    prev_s2_index, prev_repeatCount = s1_dict[s1_index % s1_len]
                    prev_repeatCount_diff = repeatCount - prev_repeatCount
                    cycle_count = (n1 * s1_len - s1_index) // (s1_len - prev_s2_index)
                    remaining_count = (n1 * s1_len - s1_index) % (s1_len - prev_s2_index)
                    repeatCount += cycle_count * prev_repeatCount_diff
                    s1_index += remaining_count
            s1_index += 1

        return repeatCount // n2
