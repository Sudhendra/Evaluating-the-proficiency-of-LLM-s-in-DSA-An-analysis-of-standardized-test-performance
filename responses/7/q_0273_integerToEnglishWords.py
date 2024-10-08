class Solution:
    
    ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    teens = ["", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    thousands = ["", "Thousand", "Million", "Billion"]
    
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        
        def helper(n):
            if n == 0:
                return ""
            elif n < 10:
                return self.ones[n] + " "
            elif n < 20:
                return self.teens[n-10] + " "
            elif n < 100:
                return self.tens[n//10] + " " + helper(n % 10)
            else:
                return self.ones[n//100] + " Hundred " + helper(n % 100)
        
        res = ""
        i = 0
        while num > 0:
            if num % 1000 != 0:
                res = helper(num % 1000) + self.thousands[i] + " " + res
            num //= 1000
            i += 1
        
        return res.strip()
