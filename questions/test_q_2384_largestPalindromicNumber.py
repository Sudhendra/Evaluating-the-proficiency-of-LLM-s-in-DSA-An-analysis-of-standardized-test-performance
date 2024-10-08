import pytest
from q_2384_largestPalindromicNumber import Solution


@pytest.mark.parametrize("num, output", [("444947137", "7449447"), ("00009", "9")])
class TestSolution:
    def test_largestPalindromic(self, num: str, output: str):
        sc = Solution()
        assert (
            sc.largestPalindromic(
                num,
            )
            == output
        )
