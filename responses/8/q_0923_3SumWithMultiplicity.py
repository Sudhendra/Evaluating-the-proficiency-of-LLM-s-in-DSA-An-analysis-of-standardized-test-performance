from collections import Counter

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        MOD = 10**9 + 7
        counts = Counter(arr)
        keys = sorted(counts)

        result = 0

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
                        result += counts[x] * counts[y] * counts[z]

                if (y + z < T) or (y + z == T and j == k):
                    j += 1
                elif y + z > T:
                    k -= 1

        for i in keys:
            T = target - 2*i
            if T != i and counts[T] > 0 and counts[i] > 0:
                result += counts[i] * (counts[i] - 1) * counts[T] // 2

        for i in keys:
            targetPair = target - i
            if counts[i] > 1 and 2*i != targetPair and counts[targetPair] > 0:
                result += counts[i] * (counts[i] - 1) // 2 * counts[targetPair]

        if target % 3 == 0 and counts.get(target // 3, 0) >= 3:
            count = counts[target // 3]
            result += count * (count - 1) * (count - 2) // 6

        return result % MOD
