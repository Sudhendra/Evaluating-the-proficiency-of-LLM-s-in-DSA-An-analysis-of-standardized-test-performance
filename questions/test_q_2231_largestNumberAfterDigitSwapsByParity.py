import pytest
from q_2231_largestNumberAfterDigitSwapsByParity import Solution


@pytest.mark.parametrize("num, output", [(1234, 3412), (65875, 87655)])
class TestSolution:
    def test_largestInteger(self, num: int, output: int):
        sc = Solution()
        assert (
            sc.largestInteger(
                num,
            )
            == output
        )
