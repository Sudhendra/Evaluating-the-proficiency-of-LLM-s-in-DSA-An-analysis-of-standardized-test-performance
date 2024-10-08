import pytest
from q_0878_nthMagicalNumber import Solution


@pytest.mark.parametrize("n, a, b, output", [(1, 2, 3, 2), (4, 2, 3, 6)])
class TestSolution:
    def test_nthMagicalNumber(self, n: int, a: int, b: int, output: int):
        sc = Solution()
        assert (
            sc.nthMagicalNumber(
                n,
                a,
                b,
            )
            == output
        )
