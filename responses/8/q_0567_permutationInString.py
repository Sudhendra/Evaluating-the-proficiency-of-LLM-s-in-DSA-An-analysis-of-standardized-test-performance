class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_counter = collections.Counter(s1)
        window_counter = collections.Counter(s2[:len(s1)])
        
        for i in range(len(s1), len(s2)):
            if s1_counter == window_counter:
                return True
            
            window_counter[s2[i - len(s1)]] -= 1
            if window_counter[s2[i - len(s1)]] == 0:
                del window_counter[s2[i - len(s1)]]
            
            window_counter[s2[i]] = window_counter.get(s2[i], 0) + 1
        
        return s1_counter == window_counter
