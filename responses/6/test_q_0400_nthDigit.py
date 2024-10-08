import pytest
from q_0400_nthDigit import Solution


@pytest.mark.parametrize("n, output", [(3, 3), (11, 0)])
class TestSolution:
    def test_findNthDigit(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.findNthDigit(
                n,
            )
            == output
        )
