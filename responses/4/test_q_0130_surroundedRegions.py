from typing import List
import pytest
from q_0130_surroundedRegions import Solution


@pytest.mark.parametrize(
    "board, output",
    [
        (
            [
                ["X", "X", "X", "X"],
                ["X", "O", "O", "X"],
                ["X", "X", "O", "X"],
                ["X", "O", "X", "X"],
            ],
            [
                ["X", "X", "X", "X"],
                ["X", "X", "X", "X"],
                ["X", "X", "X", "X"],
                ["X", "O", "X", "X"],
            ],
        ),
        ([["X"]], [["X"]]),
    ],
)
class TestSolution:
    def test_solve(self, board: List[List[str]], output: None):
        sc = Solution()
        assert (
            sc.solve(
                board,
            )
            == output
        )
