import pytest
from q_2235_addTwoIntegers import Solution


@pytest.mark.parametrize("num1, num2, output", [(12, 5, 17), (-10, 4, -6)])
class TestSolution:
    def test_sum(self, num1: int, num2: int, output: int):
        sc = Solution()
        assert (
            sc.sum(
                num1,
                num2,
            )
            == output
        )
