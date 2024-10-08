import pytest
from q_2648_generateFibonacciSequence import Solution


@pytest.mark.parametrize("callCount, output", [(5, [0, 1, 1, 2, 3]), (0, [])])
class TestSolution:
    def test_generateFibonacciSequence(self, output: Any):
        sc = Solution()
        assert (
            sc.generateFibonacciSequence(
                callCount,
            )
            == output
        )
