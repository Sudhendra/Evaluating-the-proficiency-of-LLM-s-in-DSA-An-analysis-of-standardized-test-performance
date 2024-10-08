import pytest
from q_0633_sumOfSquareNumbers import Solution


@pytest.mark.parametrize("c, output", [(5, True), (3, False)])
class TestSolution:
    def test_judgeSquareSum(self, c: int, output: bool):
        sc = Solution()
        assert (
            sc.judgeSquareSum(
                c,
            )
            == output
        )
