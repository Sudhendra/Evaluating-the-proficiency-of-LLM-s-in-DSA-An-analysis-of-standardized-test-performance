import pytest
from q_2658_maximumNumberOfFishInAGrid import Solution


@pytest.mark.parametrize(
    "grid, output",
    [
        ([[0, 2, 1, 0], [4, 0, 0, 3], [1, 0, 0, 4], [0, 3, 2, 0]], 7),
        ([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]], 1),
    ],
)
class TestSolution:
    def test_findMaxFish(self, grid: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.findMaxFish(
                grid,
            )
            == output
        )
