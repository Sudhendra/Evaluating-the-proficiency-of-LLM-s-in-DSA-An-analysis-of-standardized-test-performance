from typing import List
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        if not arr:
            return 0
        
        n = len(arr)
        num_set = set(arr)
        max_len = 0
        
        for i in range(n):
            for j in range(i + 1, n):
                a, b = arr[i], arr[j]
                curr_len = 2
                
                while a + b in num_set:
                    a, b = b, a + b
                    curr_len += 1
                
                max_len = max(max_len, curr_len)
        
        return max_len if max_len > 2 else 0
