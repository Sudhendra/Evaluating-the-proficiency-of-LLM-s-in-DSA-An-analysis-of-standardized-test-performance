class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        if not s:
            return 0

        max_length_ending_here = [0] * 26
        max_length_ending_here[ord(s[0]) - ord('a')] = 1
        result = 1

        for i in range(1, len(s)):
            if ord(s[i]) - ord(s[i-1]) == 1 or ord(s[i-1]) - ord(s[i]) == 25:
                cur_length = max_length_ending_here[ord(s[i]) - ord('a')] + 1
            else:
                cur_length = 1
            max_length_ending_here[ord(s[i]) - ord('a')] = max(max_length_ending_here[ord(s[i]) - ord('a')], cur_length)
            result += cur_length

        return result
