import pytest
from q_2132_stampingTheGrid import Solution


@pytest.mark.parametrize(
    "grid, stampHeight, stampWidth, output",
    [
        (
            [[1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]],
            4,
            3,
            True,
        ),
        ([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]], 2, 2, False),
    ],
)
class TestSolution:
    def test_possibleToStamp(
        self, grid: List[List[int]], stampHeight: int, stampWidth: int, output: bool
    ):
        sc = Solution()
        assert (
            sc.possibleToStamp(
                grid,
                stampHeight,
                stampWidth,
            )
            == output
        )
