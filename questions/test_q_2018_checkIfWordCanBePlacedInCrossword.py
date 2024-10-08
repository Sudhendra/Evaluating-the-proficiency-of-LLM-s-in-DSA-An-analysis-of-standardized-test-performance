import pytest
from q_2018_checkIfWordCanBePlacedInCrossword import Solution


@pytest.mark.parametrize(
    "board, word, output",
    [
        ([["#", " ", "#"], [" ", " ", "#"], ["#", "c", " "]], "abc", True),
        ([[" ", "#", "a"], [" ", "#", "c"], [" ", "#", "a"]], "ac", False),
        ([["#", " ", "#"], [" ", " ", "#"], ["#", " ", "c"]], "ca", True),
    ],
)
class TestSolution:
    def test_placeWordInCrossword(
        self, board: List[List[str]], word: str, output: bool
    ):
        sc = Solution()
        assert (
            sc.placeWordInCrossword(
                board,
                word,
            )
            == output
        )
