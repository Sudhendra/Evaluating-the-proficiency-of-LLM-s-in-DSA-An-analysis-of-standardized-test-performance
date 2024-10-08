class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        if not s or not t:
            return ""
        
        # Create a dictionary to store the frequency of characters in t
        dict_t = Counter(t)
        required = len(dict_t)
        
        filtered_s = []
        for i, char in enumerate(s):
            if char in dict_t:
                filtered_s.append((i, char))
        
        l, r = 0, 0
        formed = 0
        window_counts = {}
        ans = float('inf'), None, None
        
        while r < len(filtered_s):
            char = filtered_s[r][1]
            window_counts[char] = window_counts.get(char, 0) + 1
            
            if window_counts[char] == dict_t[char]:
                formed += 1
                
            while l <= r and formed == required:
                char = filtered_s[l][1]
                start = filtered_s[l][0]
                end = filtered_s[r][0]
                
                if end - start + 1 < ans[0]:
                    ans = (end - start + 1, start, end)
                
                window_counts[char] -= 1
                if window_counts[char] < dict_t[char]:
                    formed -= 1
                
                l += 1
            
            r += 1
        
        return "" if ans[0] == float('inf') else s[ans[1]:ans[2]+1]
