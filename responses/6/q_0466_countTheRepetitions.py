class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        repeat_count = 0
        index = 0
        repeat_dict = {}
        
        for i in range(1, n1 + 1):
            for ch in s1:
                if ch == s2[index]:
                    index += 1
                    if index == len(s2):
                        index = 0
                        repeat_count += 1
            
            if index in repeat_dict:
                prev_repeat_count, prev_index = repeat_dict[index]
                cycle_count = repeat_count - prev_repeat_count
                cycle_index = i - prev_index
                break
                        
            repeat_dict[index] = (repeat_count, i)
        
        if n1 < n2:
            return 0
        
        remaining_repeats = n1 - repeat_dict[index][1]
        repeat_cycle = repeat_count - repeat_dict[index][0]
        repeat_count = repeat_dict[index][0] + (remaining_repeats // repeat_cycle) * repeat_cycle
        remaining_repeats %= repeat_cycle
        
        while remaining_repeats:
            for ch in s1:
                if ch == s2[index]:
                    index += 1
                    if index == len(s2):
                        index = 0
                        repeat_count += 1
                        remaining_repeats -= 1
                        if remaining_repeats == 0:
                            break
                        
        return repeat_count // n2
