import pytest
from q_2332_theLatestTimeToCatchABus import Solution


@pytest.mark.parametrize(
    "buses, passengers, capacity, output",
    [
        ([10, 20], [2, 17, 18, 19], 2, 16),
        ([20, 30, 10], [19, 13, 26, 4, 25, 11, 21], 2, 20),
    ],
)
class TestSolution:
    def test_latestTimeCatchTheBus(
        self, buses: List[int], passengers: List[int], capacity: int, output: int
    ):
        sc = Solution()
        assert (
            sc.latestTimeCatchTheBus(
                buses,
                passengers,
                capacity,
            )
            == output
        )
