class Solution:
    def rotatedDigits(self, n: int) -> int:
        def is_good_number(num):
            good_pairs = {'0': '0', '1': '1', '8': '8', '2': '5', '5': '2', '6': '9', '9': '6'}
            num_str = str(num)
            rotated = ''

            for digit in num_str:
                if digit not in good_pairs:
                    return False
                else:
                    rotated += good_pairs[digit]

            return rotated != num_str

        count = 0
        for num in range(1, n + 1):
            if is_good_number(num):
                count += 1

        return count
