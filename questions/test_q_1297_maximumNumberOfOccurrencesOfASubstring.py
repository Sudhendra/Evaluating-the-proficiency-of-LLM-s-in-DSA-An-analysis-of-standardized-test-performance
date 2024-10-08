import pytest
from q_1297_maximumNumberOfOccurrencesOfASubstring import Solution


@pytest.mark.parametrize(
    "s, maxLetters, minSize, maxSize, output",
    [("aababcaab", 2, 3, 4, 2), ("aaaa", 1, 3, 3, 2)],
)
class TestSolution:
    def test_maxFreq(
        self, s: str, maxLetters: int, minSize: int, maxSize: int, output: int
    ):
        sc = Solution()
        assert (
            sc.maxFreq(
                s,
                maxLetters,
                minSize,
                maxSize,
            )
            == output
        )
