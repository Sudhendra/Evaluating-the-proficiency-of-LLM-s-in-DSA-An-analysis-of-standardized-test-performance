class Solution:
    def rotatedDigits(self, n: int) -> int:
        def is_good_number(num):
            num_str = str(num)
            rotated = []
            for digit in num_str:
                if digit in ['3', '4', '7']:
                    return False
                elif digit in ['2', '5', '6', '9']:
                    rotated.append(digit)
            return any(rotated)  # Check if there is a number that changes after rotation

        count = 0
        for i in range(1, n + 1):
            if is_good_number(i):
                count += 1

        return count