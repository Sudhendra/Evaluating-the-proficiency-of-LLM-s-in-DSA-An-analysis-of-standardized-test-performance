class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        cnt_s1, cnt_s2 = 0, 0
        idx_dict = {}
        
        while cnt_s1 < n1:
            for char in s1:
                if char == s2[cnt_s2]:
                    cnt_s2 += 1
                    if cnt_s2 == len(s2):
                        cnt_s2 = 0
                        idx_dict[cnt_s1] = cnt_s2
                        break
            else:
                idx_dict[cnt_s1] = cnt_s2
            cnt_s1 += 1

            if cnt_s1 in idx_dict:
                prev_cnt_s1 = idx_dict[cnt_s1]
                cycle_len = cnt_s1 - prev_cnt_s1
                remaining_cycles = (n1 - cnt_s1) // cycle_len
                cnt_s1 += remaining_cycles * cycle_len
            
        return cnt_s2 // n2