import pytest
from q_0079_wordSearch import Solution


@pytest.mark.parametrize(
    "board, word, output",
    [
        (
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            "ABCCED",
            True,
        ),
        (
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            "SEE",
            True,
        ),
        (
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            "ABCB",
            False,
        ),
    ],
)
class TestSolution:
    def test_exist(self, board: List[List[str]], word: str, output: bool):
        sc = Solution()
        assert (
            sc.exist(
                board,
                word,
            )
            == output
        )
