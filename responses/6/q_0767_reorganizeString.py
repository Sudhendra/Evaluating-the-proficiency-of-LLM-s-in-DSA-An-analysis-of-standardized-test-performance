class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        counter = collections.Counter(s)
        max_freq = max(counter.values())
        if max_freq > (n + 1) // 2:
            return ""

        res = [None] * n
        even, odd = 0, 1

        for char, count in counter.most_common():
            while count > 0 and count <= n // 2 and odd < n:
                res[odd] = char
                count -= 1
                odd += 2

            while count > 0:
                res[even] = char
                count -= 1
                even += 2

        return "".join(res)
