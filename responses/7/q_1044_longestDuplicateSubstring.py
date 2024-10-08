class Solution:
    def longestDupSubstring(self, s: str) -> str:
        def search(l, n, modulus, a, nums, s):
            h = 0
            for i in range(l):
                h = (h * a + nums[i]) % modulus
            seen = {h}
            aL = pow(a, l, modulus)

            for start in range(1, n - l + 1):
                h = (h * a - nums[start - 1] * aL + nums[start + l - 1]) % modulus
                if h in seen:
                    return start
                seen.add(h)
            return -1

        n = len(s)
        nums = [ord(c) - ord('a') for c in s]
        modulus = 2 ** 63 - 1
        a = 26

        left, right = 1, n
        res = 0
        index = -1

        while left <= right:
            mid = left + (right - left) // 2
            start = search(mid, n, modulus, a, nums, s)
            if start != -1:
                res = mid
                index = start
                left = mid + 1
            else:
                right = mid - 1

        return s[index:index + res] if res > 0 else ""
