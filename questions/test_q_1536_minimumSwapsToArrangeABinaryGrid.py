import pytest
from q_1536_minimumSwapsToArrangeABinaryGrid import Solution


@pytest.mark.parametrize(
    "grid, output",
    [
        ([[0, 0, 1], [1, 1, 0], [1, 0, 0]], 3),
        ([[0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0]], -1),
        ([[1, 0, 0], [1, 1, 0], [1, 1, 1]], 0),
    ],
)
class TestSolution:
    def test_minSwaps(self, grid: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.minSwaps(
                grid,
            )
            == output
        )
