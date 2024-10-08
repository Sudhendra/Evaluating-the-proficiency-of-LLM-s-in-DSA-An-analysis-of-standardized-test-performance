class Solution:
    def rotatedDigits(self, n: int) -> int:
        def is_good_number(num):
            valid_rotations = {'0': '0', '1': '1', '8': '8', '2': '5', '5': '2', '6': '9', '9': '6'}
            num_str = str(num)
            rotated_num = ''.join(valid_rotations[d] for d in num_str if d in valid_rotations)
            return num_str != rotated_num

        count = 0
        for i in range(1, n + 1):
            if is_good_number(i):
                count += 1

        return count
