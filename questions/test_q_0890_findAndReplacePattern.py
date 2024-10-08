import pytest
from q_0890_findAndReplacePattern import Solution


@pytest.mark.parametrize(
    "words, pattern, output",
    [
        (["abc", "deq", "mee", "aqq", "dkd", "ccc"], "abb", ["mee", "aqq"]),
        (["a", "b", "c"], "a", ["a", "b", "c"]),
    ],
)
class TestSolution:
    def test_findAndReplacePattern(
        self, words: List[str], pattern: str, output: List[str]
    ):
        sc = Solution()
        assert (
            sc.findAndReplacePattern(
                words,
                pattern,
            )
            == output
        )
