class Solution:
    def rotatedDigits(self, n: int) -> int:
        def is_good(num):
            num_str = str(num)
            rotate_map = {'0': '0', '1': '1', '2': '5', '5': '2', '6': '9', '9': '6', '8': '8'}
            rotated_num = ''.join(rotate_map.get(digit, '') for digit in num_str)
            return rotated_num != '' and rotated_num != num_str
        
        count = 0
        for num in range(1, n+1):
            if is_good(num):
                count += 1
        return count
