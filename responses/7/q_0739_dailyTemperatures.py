from typing import List

class Solution:
    
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # Initialize stack to keep track of indices of temperatures
        
        answer = [0] * len(temperatures) # Initialize answer array with zeros
        
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                answer[index] = i - index
            
            stack.append(i)
        
        return answer
