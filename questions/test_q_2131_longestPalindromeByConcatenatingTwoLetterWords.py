import pytest
from q_2131_longestPalindromeByConcatenatingTwoLetterWords import Solution


@pytest.mark.parametrize(
    "words, output",
    [
        (["lc", "cl", "gg"], 6),
        (["ab", "ty", "yt", "lc", "cl", "ab"], 8),
        (["cc", "ll", "xx"], 2),
    ],
)
class TestSolution:
    def test_longestPalindrome(self, words: List[str], output: int):
        sc = Solution()
        assert (
            sc.longestPalindrome(
                words,
            )
            == output
        )
