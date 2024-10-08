import pytest
from q_2744_findMaximumNumberOfStringPairs import Solution


@pytest.mark.parametrize(
    "words, output",
    [(["cd", "ac", "dc", "ca", "zz"], 2), (["ab", "ba", "cc"], 1), (["aa", "ab"], 0)],
)
class TestSolution:
    def test_maximumNumberOfStringPairs(self, words: List[str], output: int):
        sc = Solution()
        assert (
            sc.maximumNumberOfStringPairs(
                words,
            )
            == output
        )
