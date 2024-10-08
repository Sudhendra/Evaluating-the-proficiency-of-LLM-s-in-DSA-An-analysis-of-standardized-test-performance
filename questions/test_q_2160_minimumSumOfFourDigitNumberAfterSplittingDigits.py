import pytest
from q_2160_minimumSumOfFourDigitNumberAfterSplittingDigits import Solution


@pytest.mark.parametrize("num, output", [(2932, 52), (4009, 13)])
class TestSolution:
    def test_minimumSum(self, num: int, output: int):
        sc = Solution()
        assert (
            sc.minimumSum(
                num,
            )
            == output
        )
