import pytest
from q_0564_findTheClosestPalindrome import Solution


@pytest.mark.parametrize("n, output", [("123", "121"), ("1", "0")])
class TestSolution:
    def test_nearestPalindromic(self, n: str, output: str):
        sc = Solution()
        assert (
            sc.nearestPalindromic(
                n,
            )
            == output
        )
