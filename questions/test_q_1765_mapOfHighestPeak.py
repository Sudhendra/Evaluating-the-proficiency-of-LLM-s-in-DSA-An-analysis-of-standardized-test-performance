import pytest
from q_1765_mapOfHighestPeak import Solution


@pytest.mark.parametrize(
    "isWater, output",
    [
        ([[0, 1], [0, 0]], [[1, 0], [2, 1]]),
        ([[0, 0, 1], [1, 0, 0], [0, 0, 0]], [[1, 1, 0], [0, 1, 1], [1, 2, 2]]),
    ],
)
class TestSolution:
    def test_highestPeak(self, isWater: List[List[int]], output: List[List[int]]):
        sc = Solution()
        assert (
            sc.highestPeak(
                isWater,
            )
            == output
        )
