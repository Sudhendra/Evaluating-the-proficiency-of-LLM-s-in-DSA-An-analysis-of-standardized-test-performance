import pytest
from q_1201_uglyNumberIii import Solution


@pytest.mark.parametrize(
    "n, a, b, c, output", [(3, 2, 3, 5, 4), (4, 2, 3, 4, 6), (5, 2, 11, 13, 10)]
)
class TestSolution:
    def test_nthUglyNumber(self, n: int, a: int, b: int, c: int, output: int):
        sc = Solution()
        assert (
            sc.nthUglyNumber(
                n,
                a,
                b,
                c,
            )
            == output
        )
