from typing import List

class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        def backtrack(index, path):
            if index == len(num):
                return len(path) >= 3

            for i in range(index, len(num)):
                if num[index] == '0' and i > index:
                    break

                curr_num = int(num[index:i + 1])
                if curr_num > 2**31 - 1:
                    break

                if len(path) < 2 or curr_num == path[-1] + path[-2]:
                    path.append(curr_num)
                    if backtrack(i + 1, path):
                        return True
                    path.pop()

            return False

        res = []
        backtrack(0, res)
        return res
