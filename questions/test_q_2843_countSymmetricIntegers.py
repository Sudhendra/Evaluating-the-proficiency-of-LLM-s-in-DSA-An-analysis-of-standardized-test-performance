import pytest
from q_2843_countSymmetricIntegers import Solution


@pytest.mark.parametrize("low, high, output", [(1, 100, 9), (1200, 1230, 4)])
class TestSolution:
    def test_countSymmetricIntegers(self, low: int, high: int, output: int):
        sc = Solution()
        assert (
            sc.countSymmetricIntegers(
                low,
                high,
            )
            == output
        )
