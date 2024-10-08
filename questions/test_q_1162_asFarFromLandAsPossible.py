import pytest
from q_1162_asFarFromLandAsPossible import Solution


@pytest.mark.parametrize(
    "grid, output",
    [([[1, 0, 1], [0, 0, 0], [1, 0, 1]], 2), ([[1, 0, 0], [0, 0, 0], [0, 0, 0]], 4)],
)
class TestSolution:
    def test_maxDistance(self, grid: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.maxDistance(
                grid,
            )
            == output
        )
