class Solution:
    def binaryGap(self, n: int) -> int:
        binary = bin(n)[2:]
        max_distance = 0
        one_idx = -1

        for i in range(len(binary)):
            if binary[i] == '1':
                if one_idx != -1:
                    distance = i - one_idx
                    max_distance = max(max_distance, distance)
                one_idx = i
        
        return max_distance
