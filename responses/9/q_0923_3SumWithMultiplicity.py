class Solution:
    
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        MOD = 10**9 + 7
        count = [0] * 101
        for a in arr:
            count[a] += 1
        
        result = 0
        
        for i in range(101):
            for j in range(i, 101):
                k = target - i - j
                if k > 100 or k < 0:
                    continue
                if i == j == k:
                    result += count[i] * (count[i] - 1) * (count[i] - 2) // 6
                elif i == j != k:
                    result += count[i] * (count[i] - 1) // 2 * count[k]
                elif i < j and j < k:
                    result += count[i] * count[j] * count[k]
                    
        return result % MOD
