    def binaryGap(self, n: int) -> int:
        binary_n = bin(n)[2:]
        max_distance = 0
        prev_one = -1
        
        for i in range(len(binary_n)):
            if binary_n[i] == '1':
                if prev_one != -1:
                    distance = i - prev_one
                    max_distance = max(max_distance, distance)
                prev_one = i
        
        return max_distance
