import pytest
from q_2169_countOperationsToObtainZero import Solution


@pytest.mark.parametrize("num1, num2, output", [(2, 3, 3), (10, 10, 1)])
class TestSolution:
    def test_countOperations(self, num1: int, num2: int, output: int):
        sc = Solution()
        assert (
            sc.countOperations(
                num1,
                num2,
            )
            == output
        )
