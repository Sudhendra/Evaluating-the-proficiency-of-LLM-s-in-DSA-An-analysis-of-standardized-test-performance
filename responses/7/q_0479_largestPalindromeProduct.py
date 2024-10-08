class Solution:
    def largest_palindrome(self, n):
        if n == 1:
            return 9
        
        upper_limit = 10**n - 1
        lower_limit = upper_limit // 10
        
        for high in range(upper_limit, lower_limit, -1):
            palindrome = int(str(high) + str(high)[::-1])
            
            for i in range(upper_limit, lower_limit, -1):
                if palindrome // i > upper_limit:
                    break
                
                if palindrome % i == 0:
                    return palindrome % 1337
                
        return -1

# Example usage:
sol = Solution()
print(sol.largest_palindrome(2))  # Output: 987
print(sol.largest_palindrome(1))  # Output: 9
