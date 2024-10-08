import pytest
from q_2452_wordsWithinTwoEditsOfDictionary import Solution


@pytest.mark.parametrize(
    "queries, dictionary, output",
    [
        (
            ["word", "note", "ants", "wood"],
            ["wood", "joke", "moat"],
            ["word", "note", "wood"],
        ),
        (["yes"], ["not"], []),
    ],
)
class TestSolution:
    def test_twoEditWords(
        self, queries: List[str], dictionary: List[str], output: List[str]
    ):
        sc = Solution()
        assert (
            sc.twoEditWords(
                queries,
                dictionary,
            )
            == output
        )
