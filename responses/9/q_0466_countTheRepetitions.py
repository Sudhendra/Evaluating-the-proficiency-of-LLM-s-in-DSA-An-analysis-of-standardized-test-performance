class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        if not set(s2).issubset(set(s1)):
            return 0
        
        index_mapping = {} # Store mappings between s1 index and s2 cycle
        s1_len, s2_len = len(s1), len(s2)
        s1_idx, s2_idx, cnt = 0, 0, 0

        while True:
            for char in s1:
                if char == s2[s2_idx]:
                    s2_idx += 1
                    if s2_idx == s2_len:
                        s2_idx = 0
                        cnt += 1
            
            s1_idx += 1
            if s1_idx == s1_len:
                if s2_idx in index_mapping:
                    prev_s1_idx, prev_cnt = index_mapping[s2_idx]
                    cycle_count = (n1 - prev_s1_idx) // (s1_idx - prev_s1_idx)
                    remaining_s1_idx = (n1 - prev_s1_idx) % (s1_idx - prev_s1_idx) + prev_s1_idx
                    remaining_cnt = (n1 - prev_s1_idx) // (s1_idx - prev_s1_idx) * (cnt - prev_cnt)
                    return (prev_cnt + cycle_count * (cnt - prev_cnt) + self.getMaxRepetitions(s1[remaining_s1_idx:], n1 - remaining_s1_idx, s2, n2))
                else:
                    index_mapping[s2_idx] = (s1_idx, cnt)
                    s1_idx = 0

            if s1_idx == 0 and s2_idx == 0:
                break

        return cnt // n2

    def getMaxRepetitionsBruteForce(self, s1: str, n1: int, s2: str, n2: int) -> int:
        full_s1 = s1 * n1
        full_s2 = s2 * n2
        count = 0

        while len(full_s1) >= len(full_s2):
            if full_s2 in full_s1:
                count += 1
                full_s1 = full_s1.replace(full_s2, '', 1)
            else:
                break
        
        return count
