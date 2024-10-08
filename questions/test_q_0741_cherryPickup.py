import pytest
from q_0741_cherryPickup import Solution


@pytest.mark.parametrize(
    "grid, output",
    [
        ([[0, 1, -1], [1, 0, -1], [1, 1, 1]], 5),
        ([[1, 1, -1], [1, -1, 1], [-1, 1, 1]], 0),
    ],
)
class TestSolution:
    def test_cherryPickup(self, grid: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.cherryPickup(
                grid,
            )
            == output
        )
