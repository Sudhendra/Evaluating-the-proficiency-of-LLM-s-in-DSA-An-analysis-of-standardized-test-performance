class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return [(str(i) if i % 3 != 0 and i % 5 != 0 else 
                 ("FizzBuzz" if i % 3 == 0 and i % 5 == 0 else 
                  ("Fizz" if i % 3 == 0 else "Buzz"))) for i in range(1, n+1)]