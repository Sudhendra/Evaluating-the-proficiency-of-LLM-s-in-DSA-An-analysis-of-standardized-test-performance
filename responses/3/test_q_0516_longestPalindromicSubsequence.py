import pytest
from q_0516_longestPalindromicSubsequence import Solution


@pytest.mark.parametrize("s, output", [("bbbab", 4), ("cbbd", 2)])
class TestSolution:
    def test_longestPalindromeSubseq(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.longestPalindromeSubseq(
                s,
            )
            == output
        )
