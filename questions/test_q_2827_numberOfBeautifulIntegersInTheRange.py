import pytest
from q_2827_numberOfBeautifulIntegersInTheRange import Solution


@pytest.mark.parametrize(
    "low, high, k, output", [(10, 20, 3, 2), (1, 10, 1, 1), (5, 5, 2, 0)]
)
class TestSolution:
    def test_numberOfBeautifulIntegers(self, low: int, high: int, k: int, output: int):
        sc = Solution()
        assert (
            sc.numberOfBeautifulIntegers(
                low,
                high,
                k,
            )
            == output
        )
