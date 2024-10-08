import pytest
from q_2697_lexicographicallySmallestPalindrome import Solution


@pytest.mark.parametrize(
    "s, output", [("egcfe", "efcfe"), ("abcd", "abba"), ("seven", "neven")]
)
class TestSolution:
    def test_makeSmallestPalindrome(self, s: str, output: str):
        sc = Solution()
        assert (
            sc.makeSmallestPalindrome(
                s,
            )
            == output
        )
