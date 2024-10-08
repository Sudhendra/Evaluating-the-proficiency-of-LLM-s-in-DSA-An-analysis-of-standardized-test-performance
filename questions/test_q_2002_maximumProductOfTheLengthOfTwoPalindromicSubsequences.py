import pytest
from q_2002_maximumProductOfTheLengthOfTwoPalindromicSubsequences import Solution


@pytest.mark.parametrize(
    "s, output", [("leetcodecom", 9), ("bb", 1), ("accbcaxxcxx", 25)]
)
class TestSolution:
    def test_maxProduct(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.maxProduct(
                s,
            )
            == output
        )
