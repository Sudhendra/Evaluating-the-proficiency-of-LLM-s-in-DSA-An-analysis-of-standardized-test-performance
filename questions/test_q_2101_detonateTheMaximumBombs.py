import pytest
from q_2101_detonateTheMaximumBombs import Solution


@pytest.mark.parametrize(
    "bombs, output",
    [
        ([[2, 1, 3], [6, 1, 4]], 2),
        ([[1, 1, 5], [10, 10, 5]], 1),
        ([[1, 2, 3], [2, 3, 1], [3, 4, 2], [4, 5, 3], [5, 6, 4]], 5),
    ],
)
class TestSolution:
    def test_maximumDetonation(self, bombs: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.maximumDetonation(
                bombs,
            )
            == output
        )
