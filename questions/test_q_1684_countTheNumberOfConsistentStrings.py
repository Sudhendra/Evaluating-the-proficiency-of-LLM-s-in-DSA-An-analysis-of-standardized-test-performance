import pytest
from q_1684_countTheNumberOfConsistentStrings import Solution


@pytest.mark.parametrize(
    "allowed, words, output",
    [
        ("ab", ["ad", "bd", "aaab", "baa", "badab"], 2),
        ("abc", ["a", "b", "c", "ab", "ac", "bc", "abc"], 7),
        ("cad", ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"], 4),
    ],
)
class TestSolution:
    def test_countConsistentStrings(self, allowed: str, words: List[str], output: int):
        sc = Solution()
        assert (
            sc.countConsistentStrings(
                allowed,
                words,
            )
            == output
        )
