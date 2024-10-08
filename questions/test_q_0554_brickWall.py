import pytest
from q_0554_brickWall import Solution


@pytest.mark.parametrize(
    "wall, output",
    [
        ([[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2], [1, 3, 1, 1]], 2),
        ([[1], [1], [1]], 3),
    ],
)
class TestSolution:
    def test_leastBricks(self, wall: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.leastBricks(
                wall,
            )
            == output
        )
