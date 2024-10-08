import pytest
from q_1301_numberOfPathsWithMaxScore import Solution


@pytest.mark.parametrize(
    "board, output",
    [
        (["E23", "2X2", "12S"], [7, 1]),
        (["E12", "1X1", "21S"], [4, 2]),
        (["E11", "XXX", "11S"], [0, 0]),
    ],
)
class TestSolution:
    def test_pathsWithMaxScore(self, board: List[str], output: List[int]):
        sc = Solution()
        assert (
            sc.pathsWithMaxScore(
                board,
            )
            == output
        )
