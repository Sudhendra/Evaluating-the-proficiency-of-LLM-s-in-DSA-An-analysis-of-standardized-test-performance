import pytest
from q_1710_maximumUnitsOnATruck import Solution


@pytest.mark.parametrize(
    "boxTypes, truckSize, output",
    [([[1, 3], [2, 2], [3, 1]], 4, 8), ([[5, 10], [2, 5], [4, 7], [3, 9]], 10, 91)],
)
class TestSolution:
    def test_maximumUnits(self, boxTypes: List[List[int]], truckSize: int, output: int):
        sc = Solution()
        assert (
            sc.maximumUnits(
                boxTypes,
                truckSize,
            )
            == output
        )
