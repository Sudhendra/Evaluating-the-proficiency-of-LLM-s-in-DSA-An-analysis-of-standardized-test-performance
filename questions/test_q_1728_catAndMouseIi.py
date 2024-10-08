import pytest
from q_1728_catAndMouseIi import Solution


@pytest.mark.parametrize(
    "grid, catJump, mouseJump, output",
    [
        (["####F", "#C...", "M...."], 1, 2, True),
        (["M.C...F"], 1, 4, True),
        (["M.C...F"], 1, 3, False),
    ],
)
class TestSolution:
    def test_canMouseWin(
        self, grid: List[str], catJump: int, mouseJump: int, output: bool
    ):
        sc = Solution()
        assert (
            sc.canMouseWin(
                grid,
                catJump,
                mouseJump,
            )
            == output
        )
