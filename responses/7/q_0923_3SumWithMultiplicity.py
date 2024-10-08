from typing import List

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        MOD = 10**9 + 7
        count = [0] * 101
        for num in arr:
            count[num] += 1

        res = 0
        for i in range(101):
            for j in range(i, 101):
                k = target - i - j
                if k < 0 or k > 100:
                    continue

                if i == j == k:
                    res += count[i] * (count[i] - 1) * (count[i] - 2) // 6
                elif i == j:
                    res += count[i] * (count[i] - 1) // 2 * count[k]
                elif j < k:
                    res += count[i] * count[j] * count[k]

        return res % MOD
