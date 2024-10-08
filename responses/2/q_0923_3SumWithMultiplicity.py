class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        MOD = 10**9 + 7
        count = [0] * 101  # Since 0 <= arr[i] <= 100
        res = 0
        
        for num in arr:
            count[num] += 1
        
        for i in range(101):
            for j in range(i, 101):
                k = target - i - j
                if k < j:
                    continue
                
                if k > 100:
                    continue
                
                if i == j == k:
                    res += (count[i] * (count[i] - 1) * (count[i] - 2) // 6)
                elif i == j != k:
                    res += (count[i] * (count[i] - 1) // 2) * count[k]
                elif i < j == k:
                    res += count[i] * (count[j] * (count[j] - 1) // 2)
                elif i < j < k:
                    res += count[i] * count[j] * count[k]
        
        return res % MOD