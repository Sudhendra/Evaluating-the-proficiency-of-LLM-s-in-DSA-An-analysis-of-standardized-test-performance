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
                
                curr_num = int(num[index:i+1])
                
                if len(path) < 2 or curr_num == path[-1] + path[-2]:
                    if len(path) < 2 or curr_num <= 2**31 - 1:
                        path.append(curr_num)
                        backtrack(i+1, path)
                        if self.result:
                            return
                        path.pop()
        
        self.result = []
        backtrack(0, [])
        return self.result
