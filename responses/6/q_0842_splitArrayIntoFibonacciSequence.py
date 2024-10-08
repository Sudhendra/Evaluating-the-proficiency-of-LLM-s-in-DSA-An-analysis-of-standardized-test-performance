from typing import List

class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        def is_valid(num_str, num1, num2):
            if (num_str[0] == '0' and len(num_str) > 1) or len(str(int(num_str))) != len(num_str):
                return False
            return int(num_str) == num1 + num2

        def backtrack(start, sequence):
            if start == len(num) and len(sequence) >= 3:
                self.result = sequence[:]
                return

            for i in range(start, len(num)):
                num_str = num[start:i+1]
                if len(sequence) < 2 or is_valid(num_str, sequence[-2], sequence[-1]):
                    if len(sequence) < 2:
                        backtrack(i+1, sequence + [int(num_str)])
                    else:
                        if int(num_str) == sequence[-2] + sequence[-1]:
                            backtrack(i+1, sequence + [int(num_str)])

        self.result = []
        backtrack(0, [])
        return self.result
