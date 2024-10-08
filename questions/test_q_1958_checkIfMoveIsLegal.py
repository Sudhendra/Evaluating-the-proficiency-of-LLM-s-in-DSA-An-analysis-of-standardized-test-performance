import pytest
from q_1958_checkIfMoveIsLegal import Solution


@pytest.mark.parametrize(
    "board, rMove, cMove, color, output",
    [
        (
            [
                [".", ".", ".", "B", ".", ".", ".", "."],
                [".", ".", ".", "W", ".", ".", ".", "."],
                [".", ".", ".", "W", ".", ".", ".", "."],
                [".", ".", ".", "W", ".", ".", ".", "."],
                ["W", "B", "B", ".", "W", "W", "W", "B"],
                [".", ".", ".", "B", ".", ".", ".", "."],
                [".", ".", ".", "B", ".", ".", ".", "."],
                [".", ".", ".", "W", ".", ".", ".", "."],
            ],
            4,
            3,
            "B",
            True,
        ),
        (
            [
                [".", ".", ".", ".", ".", ".", ".", "."],
                [".", "B", ".", ".", "W", ".", ".", "."],
                [".", ".", "W", ".", ".", ".", ".", "."],
                [".", ".", ".", "W", "B", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", "B", "W", ".", "."],
                [".", ".", ".", ".", ".", ".", "W", "."],
                [".", ".", ".", ".", ".", ".", ".", "B"],
            ],
            4,
            4,
            "W",
            False,
        ),
    ],
)
class TestSolution:
    def test_checkMove(
        self, board: List[List[str]], rMove: int, cMove: int, color: str, output: bool
    ):
        sc = Solution()
        assert (
            sc.checkMove(
                board,
                rMove,
                cMove,
                color,
            )
            == output
        )
