class Solution:

    def longestSubstring(self, s: str, k: int) -> int:
        def helper(s, k, start, end):
            if end - start < k:
                return 0
            
            char_count = {}
            for i in range(start, end):
                char_count[s[i]] = char_count.get(s[i], 0) + 1
            
            for mid in range(start, end):
                if char_count[s[mid]] >= k:
                    continue
                mid_next = mid + 1
                while mid_next < end and char_count[s[mid_next]] < k:
                    mid_next += 1
                return max(helper(s, k, start, mid), helper(s, k, mid_next, end))
            
            return end - start

        return helper(s, k, 0, len(s))