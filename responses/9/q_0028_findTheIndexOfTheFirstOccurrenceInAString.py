front_matter = {
    "qid": 28,
    "title": "Find the Index of the First Occurrence in a String",
    "titleSlug": "find-the-index-of-the-first-occurrence-in-a-string",
    "difficulty": "Easy",
    "tags": ["Two Pointers", "String", "String Matching"],
}

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if needle not in haystack:
            return -1
        return haystack.index(needle)