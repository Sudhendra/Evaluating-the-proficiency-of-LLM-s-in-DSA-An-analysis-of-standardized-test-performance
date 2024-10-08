import pytest
from q_2828_checkIfAStringIsAnAcronymOfWords import Solution


@pytest.mark.parametrize(
    "words, s, output",
    [
        (["alice", "bob", "charlie"], "abc", True),
        (["an", "apple"], "a", False),
        (["never", "gonna", "give", "up", "on", "you"], "ngguoy", True),
    ],
)
class TestSolution:
    def test_isAcronym(self, words: List[str], s: str, output: bool):
        sc = Solution()
        assert (
            sc.isAcronym(
                words,
                s,
            )
            == output
        )
