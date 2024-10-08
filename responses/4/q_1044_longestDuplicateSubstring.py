class Solution:
    def longestDupSubstring(self, s: str) -> str:
        def search_LRS(L: int, n: int, base: int, mod: int, nums: List[int], s: str) -> Tuple[int, int]:
            h = 0
            for i in range(L):
                h = (h * base + nums[i]) % mod
            
            seen = {h}
            baseL = pow(base, L, mod)
            for start in range(1, n - L + 1):
                h = (h * base - nums[start - 1] * baseL + nums[start + L - 1]) % mod
                if h in seen:
                    return start, start + L
                seen.add(h)
            return -1, -1
        
        def search(s: str, L: int) -> Tuple[int, int]:
            base = 26
            mod = 2**63 - 1
            n = len(s)
            nums = [ord(c) - ord('a') for c in s]
            left, right = search_LRS(L, n, base, mod, nums, s)
            return left
        
        n = len(s)
        left, right = 1, n
        res = 0
        while left < right:
            mid = left + (right - left) // 2
            found = search(s, mid)
            if found != -1:
                left = mid + 1
                res = found
            else:
                right = mid
        
        return s[res:res+left-1]
