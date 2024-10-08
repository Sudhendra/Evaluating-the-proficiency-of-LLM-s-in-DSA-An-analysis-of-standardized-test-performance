from collections import Counter

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        count_n = Counter(str(n))
        return any(count_n == Counter(str(1 << i)) for i in range(31))
