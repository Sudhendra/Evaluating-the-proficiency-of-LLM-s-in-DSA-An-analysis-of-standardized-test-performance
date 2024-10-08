import pytest
from q_1020_numberOfEnclaves import Solution


@pytest.mark.parametrize(
    "grid, output",
    [
        ([[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]], 3),
        ([[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]], 0),
    ],
)
class TestSolution:
    def test_numEnclaves(self, grid: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.numEnclaves(
                grid,
            )
            == output
        )
