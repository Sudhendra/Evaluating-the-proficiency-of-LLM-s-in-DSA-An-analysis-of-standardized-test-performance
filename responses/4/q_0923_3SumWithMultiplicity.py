from collections import Counter

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        MOD = 10**9 + 7
        count = 0
        counter = Counter(arr)
        
        for i in range(101):
            for j in range(i, 101):
                k = target - i - j
                if k < 0 or k > 100:
                    continue
                
                if i == j == k:
                    count += counter[i] * (counter[i] - 1) * (counter[i] - 2) // 6
                elif i == j != k:
                    count += counter[i] * (counter[i] - 1) // 2 * counter[k]
                elif i < j and j < k:
                    count += counter[i] * counter[j] * counter[k]
        
        return count % MOD
