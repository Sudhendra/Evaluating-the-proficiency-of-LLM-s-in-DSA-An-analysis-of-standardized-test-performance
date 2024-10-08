from collections import Counter

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        mod = 10**9 + 7
        count = Counter(arr)
        keys = sorted(count.keys())
        total = 0

        for i, x in enumerate(keys):
            T = target - x
            j, k = i, len(keys) - 1

            while j <= k:
                y, z = keys[j], keys[k]
                if y + z < T:
                    j += 1
                elif y + z > T:
                    k -= 1
                else:
                    if i < j < k:
                        total += count[x] * count[y] * count[z]
                    elif i == j < k:
                        total += count[x] * (count[x] - 1) // 2 * count[z]
                    elif i < j == k:
                        total += count[x] * count[y] * (count[y] - 1) // 2
                    else:
                        total += count[x] * (count[x] - 1) * (count[x] - 2) // 6

                    total %= mod
                    j += 1
                    k -= 1

        return total
