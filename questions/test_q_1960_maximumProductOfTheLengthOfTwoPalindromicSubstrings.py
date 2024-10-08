import pytest
from q_1960_maximumProductOfTheLengthOfTwoPalindromicSubstrings import Solution


@pytest.mark.parametrize("s, output", [("ababbb", 9), ("zaaaxbbby", 9)])
class TestSolution:
    def test_maxProduct(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.maxProduct(
                s,
            )
            == output
        )
