import pytest
from q_0029_divideTwoIntegers import Solution


@pytest.mark.parametrize("dividend, divisor, output", [(10, 3, 3), (7, -3, -2)])
class TestSolution:
    def test_divide(self, dividend: int, divisor: int, output: int):
        sc = Solution()
        assert (
            sc.divide(
                dividend,
                divisor,
            )
            == output
        )
