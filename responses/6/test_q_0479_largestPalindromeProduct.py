import pytest
from q_0479_largestPalindromeProduct import Solution


@pytest.mark.parametrize("n, output", [(2, 987), (1, 9)])
class TestSolution:
    def test_largestPalindrome(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.largestPalindrome(
                n,
            )
            == output
        )
