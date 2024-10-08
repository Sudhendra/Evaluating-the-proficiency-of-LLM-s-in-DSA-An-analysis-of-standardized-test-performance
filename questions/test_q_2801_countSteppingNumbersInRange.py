import pytest
from q_2801_countSteppingNumbersInRange import Solution


@pytest.mark.parametrize("low, high, output", [("1", "11", 10), ("90", "101", 2)])
class TestSolution:
    def test_countSteppingNumbers(self, low: str, high: str, output: int):
        sc = Solution()
        assert (
            sc.countSteppingNumbers(
                low,
                high,
            )
            == output
        )
