import pytest
from q_1267_countServersThatCommunicate import Solution


@pytest.mark.parametrize(
    "grid, output",
    [
        ([[1, 0], [0, 1]], 0),
        ([[1, 0], [1, 1]], 3),
        ([[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]], 4),
    ],
)
class TestSolution:
    def test_countServers(self, grid: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.countServers(
                grid,
            )
            == output
        )
