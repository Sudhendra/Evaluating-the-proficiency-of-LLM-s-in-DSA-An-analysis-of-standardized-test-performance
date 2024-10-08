from typing import List

class Solution:

    def splitIntoFibonacci(self, num: str) -> List[int]:
        def backtrack(index, path):
            if index == len(num):
                return len(path) >= 3

            for i in range(index, len(num)):
                if num[index] == '0' and i > index:
                    break

                curr_num = int(num[index:i+1])
                if curr_num > 2**31 - 1:
                    break

                if len(path) < 2 or curr_num == path[-1] + path[-2]:
                    if len(path) < 2 or backtrack(i+1, path + [curr_num]):
                        return path + [curr_num]

            return []

        return backtrack(0, [])
