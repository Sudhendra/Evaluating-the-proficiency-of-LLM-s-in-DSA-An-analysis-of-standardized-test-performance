import pytest
from q_1518_waterBottles import Solution


@pytest.mark.parametrize("numBottles, numExchange, output", [(9, 3, 13), (15, 4, 19)])
class TestSolution:
    def test_numWaterBottles(self, numBottles: int, numExchange: int, output: int):
        sc = Solution()
        assert (
            sc.numWaterBottles(
                numBottles,
                numExchange,
            )
            == output
        )
