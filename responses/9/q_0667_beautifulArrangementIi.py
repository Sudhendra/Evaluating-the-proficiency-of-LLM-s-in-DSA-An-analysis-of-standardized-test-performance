from typing import List

class Solution:
    
    def constructArray(self, n: int, k: int) -> List[int]:
        result = [1]
        diff = k
        for i in range(k):
            if i % 2 == 0:
                result.append(result[-1] + diff)
            else:
                result.append(result[-1] - diff)
            diff -= 1
        result.extend(range(k + 2, n + 1))
        return result
