from typing import List

class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        def backtrack(start, path):
            if start == len(num) and len(path) >= 3:
                self.res = path[:]
                return
            for i in range(start, len(num)):
                if i > start and num[start] == '0':
                    break
                num_str = num[start:i + 1]
                if int(num_str) > 2**31 - 1:
                    break
                if len(path) < 2 or int(num_str) == path[-1] + path[-2]:
                    path.append(int(num_str))
                    backtrack(i + 1, path)
                    path.pop()
                    if self.res:
                        return

        self.res = []
        backtrack(0, [])
        return self.res if self.res else []