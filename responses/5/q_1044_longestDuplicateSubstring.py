class Solution:
    def longestDupSubstring(self, s: str) -> str:
        def search_lrs(s: str, L: int) -> str:
            base = 26
            modulus = 2**64

            def search(hash_len: int) -> str:
                hash_set = set()
                hash_val = 0
                base_power = pow(base, hash_len, modulus)

                for i in range(hash_len):
                    hash_val = (hash_val * base + ord(s[i])) % modulus
                hash_set.add(hash_val)

                for start in range(1, len(s) - hash_len + 1):
                    hash_val = (hash_val * base - ord(s[start - 1]) * base_power + ord(s[start + hash_len - 1])) % modulus
                    if hash_val in hash_set:
                        return s[start:start + hash_len]
                    hash_set.add(hash_val)

                return ""

            left, right = 1, len(s)
            result = ""
            while left <= right:
                mid = left + (right - left) // 2
                lrs = search(mid)
                if lrs:
                    result = lrs
                    left = mid + 1
                else:
                    right = mid - 1
                    
            return result

        return search_lrs(s, len(s))
