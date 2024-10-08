import pytest
from q_1969_minimumNonZeroProductOfTheArrayElements import Solution


@pytest.mark.parametrize("p, output", [(1, 1), (2, 6), (3, 1512)])
class TestSolution:
    def test_minNonZeroProduct(self, p: int, output: int):
        sc = Solution()
        assert (
            sc.minNonZeroProduct(
                p,
            )
            == output
        )
