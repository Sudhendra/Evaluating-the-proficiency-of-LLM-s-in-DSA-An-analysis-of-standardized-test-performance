front_matter = {
    "qid": 854,
    "title": "K-Similar Strings",
    "titleSlug": "k-similar-strings",
    "difficulty": "Hard",
    "tags": ["String", "Breadth-First Search"],
}

class Solution:
    """Strings `s1` and `s2` are `k`**-similar** (for some non-negative integer `k`) if we can swap the positions of two letters in `s1` exactly `k` times so that the resulting string equals `s2`.

    Given two anagrams `s1` and `s2`, return the smallest `k` for which `s1` and `s2` are `k`**-similar**.
    """
    
    def kSimilarity(self, s1: str, s2: str) -> int:
        def neighbors(s: str) -> List[str]:
            res = []
            i = 0
            while s[i] == s2[i]:
                i += 1
            for j in range(i + 1, len(s)):
                if s[j] == s2[i]:
                    slist = list(s)
                    slist[i], slist[j] = slist[j], slist[i]
                    res.append("".join(slist))
            return res
        
        q = [(s1, 0)]
        visited = set()
        
        while q:
            cur, k = q.pop(0)
            if cur == s2:
                return k
            if cur not in visited:
                visited.add(cur)
                for nei in neighbors(cur):
                    q.append((nei, k + 1))