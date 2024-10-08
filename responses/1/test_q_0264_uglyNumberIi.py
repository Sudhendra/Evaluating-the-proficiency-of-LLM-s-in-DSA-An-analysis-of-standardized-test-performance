import pytest
from q_0264_uglyNumberIi import Solution


@pytest.mark.parametrize("n, output", [(10, 12), (1, 1)])
class TestSolution:
    def test_nthUglyNumber(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.nthUglyNumber(
                n,
            )
            == output
        )
