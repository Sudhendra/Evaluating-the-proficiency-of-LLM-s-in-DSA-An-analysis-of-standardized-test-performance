import pytest
from q_3100_waterBottlesIi import Solution


@pytest.mark.parametrize("numBottles, numExchange, output", [(13, 6, 15), (10, 3, 13)])
class TestSolution:
    def test_maxBottlesDrunk(self, numBottles: int, numExchange: int, output: int):
        sc = Solution()
        assert (
            sc.maxBottlesDrunk(
                numBottles,
                numExchange,
            )
            == output
        )
