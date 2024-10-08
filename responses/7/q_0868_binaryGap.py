class Solution:
    def binaryGap(self, n: int) -> int:
        b = bin(n)[2:]
        max_gap = 0
        last_idx = -1
        
        for i in range(len(b)):
            if b[i] == '1':
                if last_idx != -1:
                    max_gap = max(max_gap, i - last_idx)
                last_idx = i
        
        return max_gap
