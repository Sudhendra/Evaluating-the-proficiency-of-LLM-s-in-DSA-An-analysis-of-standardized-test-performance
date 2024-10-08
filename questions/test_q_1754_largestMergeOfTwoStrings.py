import pytest
from q_1754_largestMergeOfTwoStrings import Solution


@pytest.mark.parametrize(
    "word1, word2, output",
    [("cabaa", "bcaaa", "cbcabaaaaa"), ("abcabc", "abdcaba", "abdcabcabcaba")],
)
class TestSolution:
    def test_largestMerge(self, word1: str, word2: str, output: str):
        sc = Solution()
        assert (
            sc.largestMerge(
                word1,
                word2,
            )
            == output
        )
