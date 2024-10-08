class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        num_str = list(str(n))

        length = len(num_str)
        index = length
        for i in range(length - 1, 0, -1):
            if int(num_str[i]) < int(num_str[i - 1]):
                num_str[i - 1] = str(int(num_str[i - 1]) - 1)
                index= i
        
        for i in range(index, length):
            num_str[i] = '9'
        
        return int(''.join(num_str))
