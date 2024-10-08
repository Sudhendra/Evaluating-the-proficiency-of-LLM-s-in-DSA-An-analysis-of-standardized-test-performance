class Solution:
    
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        n_str = str(n)
        n_len = len(n_str)
        digits_set = set(digits)
        result = sum(len(digits) ** i for i in range(1, n_len))
        
        for i in range(n_len):
            result += sum(1 for d in digits if d < n_str[i]) * len(digits) ** (n_len - i - 1)
            if n_str[i] not in digits_set:
                break
            if i == n_len - 1:
                result += 1
        
        return result