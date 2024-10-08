class Solution:
    def binaryGap(self, n: int) -> int:
        binary_str = bin(n)[2:]
        max_distance = 0
        distance = 0
        found_one = False
        
        for char in binary_str:
            if char == '1':
                if found_one:
                    max_distance = max(max_distance, distance)
                    distance = 1
                else:
                    found_one = True
            elif found_one:
                distance += 1
        
        return max_distance