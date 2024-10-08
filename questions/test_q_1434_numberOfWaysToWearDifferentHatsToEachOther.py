import pytest
from q_1434_numberOfWaysToWearDifferentHatsToEachOther import Solution


@pytest.mark.parametrize(
    "hats, output",
    [
        ([[3, 4], [4, 5], [5]], 1),
        ([[3, 5, 1], [3, 5]], 4),
        ([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]], 24),
    ],
)
class TestSolution:
    def test_numberWays(self, hats: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.numberWays(
                hats,
            )
            == output
        )
