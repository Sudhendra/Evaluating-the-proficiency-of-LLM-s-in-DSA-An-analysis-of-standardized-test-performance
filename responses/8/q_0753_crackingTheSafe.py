from typing import List

class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        total_combinations = k ** n
        seen = set()
        ans = []

        for i in range(total_combinations):
            current = ""
            for j in range(n):
                current += str(i % k)
                i //= k
            if i > 0:
                continue
            if current in seen:
                continue
            seen.add(current)
            for j in range(1, len(current)):
                seen.add(current[j:])
            ans.append(current)

        return "".join(ans) + "0" * (n-1)
