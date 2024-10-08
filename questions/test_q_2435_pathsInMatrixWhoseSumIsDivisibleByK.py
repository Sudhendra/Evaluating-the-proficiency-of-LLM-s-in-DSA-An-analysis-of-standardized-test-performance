import pytest
from q_2435_pathsInMatrixWhoseSumIsDivisibleByK import Solution


@pytest.mark.parametrize(
    "grid, k, output",
    [
        ([[5, 2, 4], [3, 0, 5], [0, 7, 2]], 3, 2),
        ([[0, 0]], 5, 1),
        ([[7, 3, 4, 9], [2, 3, 6, 2], [2, 3, 7, 0]], 1, 10),
    ],
)
class TestSolution:
    def test_numberOfPaths(self, grid: List[List[int]], k: int, output: int):
        sc = Solution()
        assert (
            sc.numberOfPaths(
                grid,
                k,
            )
            == output
        )
