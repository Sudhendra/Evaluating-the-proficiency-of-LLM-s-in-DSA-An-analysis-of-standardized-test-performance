import pytest
from q_0829_consecutiveNumbersSum import Solution


@pytest.mark.parametrize("n, output", [(5, 2), (9, 3), (15, 4)])
class TestSolution:
    def test_consecutiveNumbersSum(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.consecutiveNumbersSum(
                n,
            )
            == output
        )
