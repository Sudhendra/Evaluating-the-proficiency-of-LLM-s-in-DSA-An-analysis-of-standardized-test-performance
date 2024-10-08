import pytest
from q_0883_projectionAreaOf3DShapes import Solution


@pytest.mark.parametrize(
    "grid, output", [([[1, 2], [3, 4]], 17), ([[2]], 5), ([[1, 0], [0, 2]], 8)]
)
class TestSolution:
    def test_projectionArea(self, grid: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.projectionArea(
                grid,
            )
            == output
        )
