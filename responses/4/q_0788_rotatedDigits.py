class Solution:
    def rotatedDigits(self, n: int) -> int:
        count = 0
        for num in range(1, n+1):
            num_str = str(num)
            if any(d in num_str for d in ["3", "4", "7"]):
                continue
            if any(d in num_str for d in ["2", "5", "6", "9"]):
                count += 1
        return count
