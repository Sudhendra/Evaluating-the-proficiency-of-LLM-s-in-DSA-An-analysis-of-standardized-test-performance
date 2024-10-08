import pytest
from q_0134_gasStation import Solution


@pytest.mark.parametrize(
    "gas, cost, output",
    [([1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 3), ([2, 3, 4], [3, 4, 3], -1)],
)
class TestSolution:
    def test_canCompleteCircuit(self, gas: List[int], cost: List[int], output: int):
        sc = Solution()
        assert (
            sc.canCompleteCircuit(
                gas,
                cost,
            )
            == output
        )
