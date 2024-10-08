import pytest
from q_1802_maximumValueAtAGivenIndexInABoundedArray import Solution


@pytest.mark.parametrize("n, index, maxSum, output", [(4, 2, 6, 2), (6, 1, 10, 3)])
class TestSolution:
    def test_maxValue(self, n: int, index: int, maxSum: int, output: int):
        sc = Solution()
        assert (
            sc.maxValue(
                n,
                index,
                maxSum,
            )
            == output
        )
