from typing import List

class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        def backtrack(index, path):
            if index == len(num) and len(path) >= 3:
                self.result = path[:]
                return

            for i in range(index, len(num)):
                if num[index] == '0' and i > index:
                    break

                num_str = num[index:i+1]
                num_int = int(num_str)

                if num_int > 2**31 - 1:
                    break

                if len(path) < 2 or num_int == path[-1] + path[-2]:
                    path.append(num_int)
                    backtrack(i + 1, path)
                    path.pop()

        self.result = []
        backtrack(0, [])
        return self.result
