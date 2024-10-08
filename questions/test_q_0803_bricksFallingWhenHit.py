import pytest
from q_0803_bricksFallingWhenHit import Solution


@pytest.mark.parametrize(
    "grid, hits, output",
    [
        ([[1, 0, 0, 0], [1, 1, 1, 0]], [[1, 0]], [2]),
        ([[1, 0, 0, 0], [1, 1, 0, 0]], [[1, 1], [1, 0]], [0, 0]),
    ],
)
class TestSolution:
    def test_hitBricks(
        self, grid: List[List[int]], hits: List[List[int]], output: List[int]
    ):
        sc = Solution()
        assert (
            sc.hitBricks(
                grid,
                hits,
            )
            == output
        )
