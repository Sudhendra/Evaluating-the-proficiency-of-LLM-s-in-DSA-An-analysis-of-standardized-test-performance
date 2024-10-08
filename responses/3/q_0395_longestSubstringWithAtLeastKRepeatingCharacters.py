class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def divide_and_conquer(s, k, start, end):
            if end < start:
                return 0
            
            char_counts = {}
            for i in range(start, end):
                char_counts[s[i]] = char_counts.get(s[i], 0) + 1
            
            for mid in range(start, end):
                if char_counts[s[mid]] >= k:
                    continue
                
                mid_next = mid + 1
                while mid_next < end and char_counts[s[mid_next]] < k:
                    mid_next += 1
                    
                return max(divide_and_conquer(s, k, start, mid), divide_and_conquer(s, k, mid_next, end))
            
            return end - start
        
        return divide_and_conquer(s, k, 0, len(s))
