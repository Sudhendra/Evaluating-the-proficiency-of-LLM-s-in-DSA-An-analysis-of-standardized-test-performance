import pytest
from q_2255_countPrefixesOfAGivenString import Solution


@pytest.mark.parametrize(
    "words, s, output",
    [(["a", "b", "c", "ab", "bc", "abc"], "abc", 3), (["a", "a"], "aa", 2)],
)
class TestSolution:
    def test_countPrefixes(self, words: List[str], s: str, output: int):
        sc = Solution()
        assert (
            sc.countPrefixes(
                words,
                s,
            )
            == output
        )
