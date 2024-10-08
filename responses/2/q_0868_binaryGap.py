class Solution:
    def binaryGap(self, n: int) -> int:
        binary_str = bin(n)[2:]
        max_distance = 0
        first_one_index = binary_str.find('1')
        prev_one_index = first_one_index

        for i in range(first_one_index + 1, len(binary_str)):
            if binary_str[i] == '1':
                max_distance = max(max_distance, i - prev_one_index)
                prev_one_index = i

        return max_distance