class Solution:
    def binaryGap(self, n: int) -> int:
        max_distance = 0
        current_distance = 0
        has_one = False

        while n > 0:
            if n & 1:
                if has_one:
                    max_distance = max(max_distance, current_distance)
                    current_distance = 1
                else:
                    has_one = True
            elif has_one:
                current_distance += 1
            
            n >>= 1

        return max_distance
