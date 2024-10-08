import pytest
from q_2749_minimumOperationsToMakeTheIntegerZero import Solution


@pytest.mark.parametrize("num1, num2, output", [(3, -2, 3), (5, 7, -1)])
class TestSolution:
    def test_makeTheIntegerZero(self, num1: int, num2: int, output: int):
        sc = Solution()
        assert (
            sc.makeTheIntegerZero(
                num1,
                num2,
            )
            == output
        )
