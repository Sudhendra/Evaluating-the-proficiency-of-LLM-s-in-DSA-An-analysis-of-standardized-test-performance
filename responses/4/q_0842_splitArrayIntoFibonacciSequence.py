from typing import List

class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        max_int = 2**31 - 1

        def is_valid(num_str):
            return len(num_str) == 1 or num_str[0] != '0'

        def backtrack(start, f):
            if start == len(num) and len(f) >= 3:
                return f
            for end in range(start + 1, len(num) + 1):
                num_str = num[start:end]
                if (len(num_str) > len(str(max_int)) or
                        (len(num_str) == len(str(max_int)) and int(num_str) > max_int)):
                    break
                if is_valid(num_str) and len(f) < 2 or int(num_str) == f[-1] + f[-2]:
                    res = backtrack(end, f + [int(num_str)])
                    if res:
                        return res
            return []

        return backtrack(0, [])

# Example usage
solution = Solution()
num = "1101111"
print(solution.splitIntoFibonacci(num))  # Output: [11, 0, 11, 11]
