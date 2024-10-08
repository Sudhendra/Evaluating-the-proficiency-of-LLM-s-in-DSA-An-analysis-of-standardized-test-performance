import pytest
from q_1523_countOddNumbersInAnIntervalRange import Solution


@pytest.mark.parametrize("low, high, output", [(3, 7, 3), (8, 10, 1)])
class TestSolution:
    def test_countOdds(self, low: int, high: int, output: int):
        sc = Solution()
        assert (
            sc.countOdds(
                low,
                high,
            )
            == output
        )
