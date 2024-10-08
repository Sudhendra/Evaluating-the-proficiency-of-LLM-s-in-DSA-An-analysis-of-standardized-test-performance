import pytest
from q_1771_maximizePalindromeLengthFromSubsequences import Solution


@pytest.mark.parametrize(
    "word1, word2, output", [("cacb", "cbba", 5), ("ab", "ab", 3), ("aa", "bb", 0)]
)
class TestSolution:
    def test_longestPalindrome(self, word1: str, word2: str, output: int):
        sc = Solution()
        assert (
            sc.longestPalindrome(
                word1,
                word2,
            )
            == output
        )
