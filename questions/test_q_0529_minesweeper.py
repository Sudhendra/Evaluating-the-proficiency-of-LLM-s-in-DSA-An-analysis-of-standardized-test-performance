import pytest
from q_0529_minesweeper import Solution


@pytest.mark.parametrize(
    "board, click, output",
    [
        (
            [
                ["E", "E", "E", "E", "E"],
                ["E", "E", "M", "E", "E"],
                ["E", "E", "E", "E", "E"],
                ["E", "E", "E", "E", "E"],
            ],
            [3, 0],
            [
                ["B", "1", "E", "1", "B"],
                ["B", "1", "M", "1", "B"],
                ["B", "1", "1", "1", "B"],
                ["B", "B", "B", "B", "B"],
            ],
        ),
        (
            [
                ["B", "1", "E", "1", "B"],
                ["B", "1", "M", "1", "B"],
                ["B", "1", "1", "1", "B"],
                ["B", "B", "B", "B", "B"],
            ],
            [1, 2],
            [
                ["B", "1", "E", "1", "B"],
                ["B", "1", "X", "1", "B"],
                ["B", "1", "1", "1", "B"],
                ["B", "B", "B", "B", "B"],
            ],
        ),
    ],
)
class TestSolution:
    def test_updateBoard(
        self, board: List[List[str]], click: List[int], output: List[List[str]]
    ):
        sc = Solution()
        assert (
            sc.updateBoard(
                board,
                click,
            )
            == output
        )
