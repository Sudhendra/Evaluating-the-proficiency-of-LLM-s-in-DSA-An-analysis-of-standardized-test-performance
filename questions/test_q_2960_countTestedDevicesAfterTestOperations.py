import pytest
from q_2960_countTestedDevicesAfterTestOperations import Solution


@pytest.mark.parametrize(
    "batteryPercentages, output", [([1, 1, 2, 1, 3], 3), ([0, 1, 2], 2)]
)
class TestSolution:
    def test_countTestedDevices(self, batteryPercentages: List[int], output: int):
        sc = Solution()
        assert (
            sc.countTestedDevices(
                batteryPercentages,
            )
            == output
        )
