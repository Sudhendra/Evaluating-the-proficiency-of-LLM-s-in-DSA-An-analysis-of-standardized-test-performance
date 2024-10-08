class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_count = Counter(s1)
        s2_count = Counter(s2[:len(s1) - 1])
        
        for i in range(len(s1) - 1, len(s2)):
            s2_count[s2[i]] += 1
            if s2_count == s1_count:
                return True
            s2_count[s2[i - len(s1) + 1]] -= 1
            if s2_count[s2[i - len(s1) + 1]] == 0:
                del s2_count[s2[i - len(s1) + 1]]
        
        return False
