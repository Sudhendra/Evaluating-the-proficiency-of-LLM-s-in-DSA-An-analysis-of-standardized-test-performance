class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        result = []
        text_list = text.split()
        n = len(text_list)
        
        for i in range(n - 2):
            if text_list[i] == first and text_list[i + 1] == second:
                result.append(text_list[i + 2])
        
        return result
