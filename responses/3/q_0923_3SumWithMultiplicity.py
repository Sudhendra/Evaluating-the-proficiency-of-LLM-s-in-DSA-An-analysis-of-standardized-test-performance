from collections import Counter

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        MOD = 10**9 + 7
        count = Counter(arr)
        keys = sorted(count)

        res = 0
        for i, x in enumerate(keys):
            target2 = target - x
            target2_count = target2
            j, k = 0, len(keys) - 1

            while j <= k:
                y, z = keys[j], keys[k]
                if y + z < target2:
                    j += 1
                elif y + z > target2:
                    k -= 1
                else:
                    if i < j < k:
                        res = (res + count[x] * count[y] * count[z]) % MOD
                    elif i == j < k:
                        res = (res + count[x] * (count[x] - 1) // 2 * count[z]) % MOD
                    elif i < j == k:
                        res = (res + count[x] * count[y] * (count[y] - 1) // 2) % MOD
                    else:
                        res = (res + count[x] * (count[x] - 1) * (count[x] - 2) // 6) % MOD
                    j += 1
                    k -= 1

        return res
