from typing import List

class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        def backtrack(index, path):
            if index == len(num) and len(path) >= 3:
                self.result = path.copy()
                return True

            for i in range(index, len(num)):
                if num[index] == "0" and i > index:  # to handle leading zeros
                    break

                num_str = num[index:i+1]
                if num_str and int(num_str) < 2**31:  # to handle integer overflow
                    num_val = int(num_str)
                    if len(path) < 2 or (num_val == path[-1] + path[-2]):
                        path.append(num_val)
                        if backtrack(i+1, path):
                            return True
                        path.pop()

            return False

        self.result = []
        backtrack(0, [])
        return self.result if self.result else []