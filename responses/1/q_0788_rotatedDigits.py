class Solution:
    def rotatedDigits(self, n: int) -> int:
        def is_good(num):
            valid_set = {'2', '5', '6', '9', '0', '1', '8'}
            rotate_map = {'0': '0', '1': '1', '8': '8', '2': '5', '5': '2', '6': '9', '9': '6'}

            num_str = str(num)
            rotated_str = ''
            for digit in num_str:
                if digit not in valid_set:
                    return False
                rotated_str += rotate_map[digit]
            return num_str != rotated_str

        count = 0
        for num in range(1, n + 1):
            if is_good(num):
                count += 1
        return count