from collections import Counter

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        MOD = 10**9 + 7
        res = 0
        counter = Counter(arr)

        for i in range(101):
            for j in range(i, 101):
                k = target - i - j
                if k < 0 or k > 100:
                    continue
                if i == j == k:
                    res += counter[i] * (counter[i] - 1) * (counter[i] - 2) // 6
                elif i == j:
                    res += counter[i] * (counter[i] - 1) // 2 * counter[k]
                elif j < k:
                    res += counter[i] * counter[j] * counter[k]

        return res % MOD
