import pytest
from q_1967_numberOfStringsThatAppearAsSubstringsInWord import Solution


@pytest.mark.parametrize(
    "patterns, word, output",
    [
        (["a", "abc", "bc", "d"], "abc", 3),
        (["a", "b", "c"], "aaaaabbbbb", 2),
        (["a", "a", "a"], "ab", 3),
    ],
)
class TestSolution:
    def test_numOfStrings(self, patterns: List[str], word: str, output: int):
        sc = Solution()
        assert (
            sc.numOfStrings(
                patterns,
                word,
            )
            == output
        )
