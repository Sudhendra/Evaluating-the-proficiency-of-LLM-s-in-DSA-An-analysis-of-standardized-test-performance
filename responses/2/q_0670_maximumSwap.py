class Solution:
    def maximumSwap(self, num: int) -> int:
        num_str = list(str(num))
        n = len(num_str)
        digit_last_seen = {int(num_str[i]): i for i in range(n)}

        for i in range(n):
            for d in range(9, int(num_str[i]), -1): # Start from 9 and go till the digit before num_str[i] in descending order
                if d in digit_last_seen and digit_last_seen[d] > i: 
                    num_str[i], num_str[digit_last_seen[d]] = num_str[digit_last_seen[d]], num_str[i] # Swap the digits
                    return int(''.join(num_str))
        
        return num