class Solution:
    def longestDupSubstring(self, s: str) -> str:
        def search(s, length, modulus):
            hash_set = set()
            base = 26
            n = len(s)
            base_power = pow(base, length, modulus)
            hash_value = 0
            for i in range(length):
                hash_value = (hash_value * base + ord(s[i]) - ord('a')) % modulus

            hash_set.add(hash_value)
            for i in range(1, n - length + 1):
                hash_value = (hash_value * base - (ord(s[i - 1]) - ord('a')) * base_power + ord(s[i + length - 1]) - ord('a')) % modulus
                if hash_value in hash_set:
                    return i
                hash_set.add(hash_value)
            
            return -1

        def longest_duplicate_substring(s):
            n = len(s)
            modulus = 2**63 - 1
            left, right = 1, n
            result = ""
            while left <= right:
                mid = left + (right - left) // 2
                index = search(s, mid, modulus)
                if index != -1:
                    result = s[index:index + mid]
                    left = mid + 1
                else:
                    right = mid - 1
            return result

        return longest_duplicate_substring(s)
