import pytest
from q_2279_maximumBagsWithFullCapacityOfRocks import Solution


@pytest.mark.parametrize(
    "capacity, rocks, additionalRocks, output",
    [([2, 3, 4, 5], [1, 2, 4, 4], 2, 3), ([10, 2, 2], [2, 2, 0], 100, 3)],
)
class TestSolution:
    def test_maximumBags(
        self, capacity: List[int], rocks: List[int], additionalRocks: int, output: int
    ):
        sc = Solution()
        assert (
            sc.maximumBags(
                capacity,
                rocks,
                additionalRocks,
            )
            == output
        )
