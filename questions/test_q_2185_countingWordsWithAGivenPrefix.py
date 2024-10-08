import pytest
from q_2185_countingWordsWithAGivenPrefix import Solution


@pytest.mark.parametrize(
    "words, pref, output",
    [
        (["pay", "**at**tention", "practice", "**at**tend"], "at", 2),
        (["leetcode", "win", "loops", "success"], "code", 0),
    ],
)
class TestSolution:
    def test_prefixCount(self, words: List[str], pref: str, output: int):
        sc = Solution()
        assert (
            sc.prefixCount(
                words,
                pref,
            )
            == output
        )
