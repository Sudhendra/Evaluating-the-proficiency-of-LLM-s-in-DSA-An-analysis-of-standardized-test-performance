class Solution:
    def nearestPalindromic(self, n: str) -> str:
        if len(n) == 1:  # edge case for single digit number
            return str(int(n) - 1)
        
        length = len(n)
        candidates = set()
        candidates.add("1" + "0" * (length - 1) + "1")  # smallest palindrome with the same length
        candidates.add("9" * (length - 1))  # largest palindrome with the same length
        candidates.add(str(10 ** length + 1))  # next palindrome after n with +1 digit
        
        prefix = int(n[:(length + 1) // 2])
        for i in range(-1, 2):
            prefix_str = str(prefix + i)
            if length % 2 == 0:  # even length, need to check two prefixes
                candidate = prefix_str + prefix_str[::-1]
                candidates.add(candidate)
            else:  # odd length, only need to check one prefix
                candidate = prefix_str + prefix_str[-2::-1]
                candidates.add(candidate)
                
        min_diff = float('inf')
        res = ""
        num = int(n)
        for candidate in candidates:
            candidate_num = int(candidate)
            if candidate_num == num:
                continue
            diff = abs(candidate_num - num)
            if diff < min_diff or (diff == min_diff and candidate_num < int(res)):
                min_diff = diff
                res = candidate
                
        return res