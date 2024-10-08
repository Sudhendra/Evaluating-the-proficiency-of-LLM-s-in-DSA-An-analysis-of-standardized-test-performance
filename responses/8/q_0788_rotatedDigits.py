class Solution:
    
    def rotatedDigits(self, n: int) -> int:
        count = 0
        for num in range(1, n+1):
            num_str = str(num)
            if '3' in num_str or '4' in num_str or '7' in num_str:
                continue
            if '2' in num_str or '5' in num_str or '6' in num_str or '9' in num_str:
                count += 1
        return count
