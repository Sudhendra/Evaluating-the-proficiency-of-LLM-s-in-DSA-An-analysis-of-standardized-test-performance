import pytest
from q_1414_findTheMinimumNumberOfFibonacciNumbersWhoseSumIsK import Solution


@pytest.mark.parametrize("k, output", [(7, 2), (10, 2), (19, 3)])
class TestSolution:
    def test_findMinFibonacciNumbers(self, k: int, output: int):
        sc = Solution()
        assert (
            sc.findMinFibonacciNumbers(
                k,
            )
            == output
        )
