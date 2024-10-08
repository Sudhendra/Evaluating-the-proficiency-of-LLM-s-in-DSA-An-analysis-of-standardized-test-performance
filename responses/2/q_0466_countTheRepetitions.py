class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        if n1 == 0:
            return 0
        
        count = 0
        index = 0
        repeat_count = {}
        s1_length = len(s1)
        s2_length = len(s2)
        
        for i in range(1, n1 + 1):
            for j in range(s1_length):
                if s1[j] == s2[index]:
                    index += 1
                    if index == s2_length:
                        index = 0
                        count += 1
            
            if index in repeat_count:
                prev_count = repeat_count[index]
                cycle_length = i - prev_count
                cycle_count = (n1 - i) // cycle_length
                count_diff = count - prev_count
                count += cycle_count * count_diff
                i = i + cycle_count * cycle_length
            else:
                repeat_count[index] = i
        
        return count // n2        